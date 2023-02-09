library(pacman)
p_load(BGLR, BEDMatrix)

################################################################
### define function to write genotype matrix from R to plink ###
################################################################

#' @name WritePlink
#' @title Write an array of integer genotypes to a binary plink file
#' @author Claas Heuer
#' @usage 
#' WritePlink(M, file_out)
#' @description
#' Based on a character array where genotypes are coded as AA,AB,BB,NA, write
#' out a column major binary plink file using \code{BGLR}'s \code{write_bed}
#' @param M 
#' \code{integer array} of genotypes in 0,1,2 coding
#' @param file_out 
#' \code{character} filename for output
#' @examples
#'
#'
#' # Now write that array to a binary plink file
#' file_out <- paste(tempdir(), "testOut.bed", sep = "/")
#' WritePlink(Mchar, file_out)
#'
#' # check if everything worked as expected
#' m <- as(BEDMatrix(file_out), "matrix")

#' @export
WritePlink <- function(M, file_out) {

	if(!is.integer(M) | !is.array(M)) stop("M must be a integer array/matrix")
	if(is.null(colnames(M))) stop("M must have column names")
	if(is.null(rownames(M))) stop("M must have row names")

	# seperate file into path and name
	path = dirname(file_out)

	if(!dir.exists(path)) dir.create(path, recursive = TRUE)
	file = basename(file_out)

	file <- gsub("\\.bed$", "", file)

	# now create the integer vector
	x <- integer(length = prod(dim(M)))

	# this is the coding BGLR's write_bed is expecting:
	#
	# Integer code Genotype
	# 0 00 Homozygote "1"/"1"
	# 1 01 Heterozygote
	# 2 10 Missing genotype
	# 3 11 Homozygote "2"/"2"

	# we can map the matrix elements from M directly to the integer vector
	# because both are column major
	x[M == 0] <- 0
	x[M == 1] <- 1
	x[M == 2] <- 3
	x[is.na(M)] <- 2

	# write_bed only returns the binary file, not the necessary .fam and .bim files.
	# We create those here now
	bim <- data.frame(Chromosome = 0,
			  VariantIdentifier = colnames(M),
			  BasePairCoordinate = 0,
			  Position = 0,
			  AlleleOne = "A",
			  AllelTwo = "B",
			  stringsAsFactors = FALSE)

	# and the fam file (https://www.cog-genomics.org/plink2/formats#fam)
	fam <- data.frame(FamilyID = rownames(M),
			  WithinFamilyID = rownames(M),
			  Sire = 0,
			  Dam = 0,
			  Sex = 0,
			  Phenotype = 0,
			  stringsAsFactors = FALSE)

	# write everything to file
	write.table(bim, file = paste(path, "/", file, ".bim", sep = ""),
		    col.names = FALSE, row.names = FALSE, quote = FALSE, sep = "\t")

	write.table(fam, file = paste(path, "/", file, ".fam", sep = ""),
		    col.names = FALSE, row.names = FALSE, quote = FALSE, sep = "\t")

	# and the bed file using BGLR's write_bed()
	tmp <- BGLR::write_bed(x = x, n = nrow(M), p = ncol(M), 
			       bed_file = paste(path, "/", file, ".bed", sep = ""))

}

##################
### Example of ###
##################

# 1. use BGLR example mice data as genotype source
# 2. use WritePlink to generate plink file
# 3. use BEDMatrix to map plink file back to a "virtual" matrix object
# 4. extract records from BEDMatrix into R matrix

data(mice, package = "BGLR")

# the genotype matrix
M = mice.X

# change data type from numeric (double) to integer
# NOTE: this is just to make sure we dont have floats in the genotypes
mode(M) = "integer"

# write plink file
temp_dir = tempdir()
file_out = paste(temp_dir, "my_plink_file", sep = "/")

WritePlink(M = M, file_out = file_out)

# show the files generated
list.files(temp_dir)

# map the plink file to BEDMatrix object
# NOTE: that object stores row and column names, but does not 
# store the genotype data in memory
BM = BEDMatrix(file_out)

# rownames of BEDMatrix is subject_family; get rid of family id
rownames(BM) = gsub("_.*", "", rownames(BM))

# extract specific rows to R matrix
ids_in = rownames(M)[sample(1:nrow(M), round(nrow(M) * 0.3, digits = 0), replace = FALSE)]

M_from_bed = BM[match(ids_in, rownames(BM)),]

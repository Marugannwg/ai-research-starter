# Compute Krippendorff's alpha (nominal) using R
# Input: data/pilot_labels.csv with columns: unit,rater,label
# install.packages(c('irr','tidyr','dplyr'))
library(irr)
library(tidyr)
library(dplyr)

df <- read.csv('data/pilot_labels.csv', stringsAsFactors = FALSE)
wide <- df %>% tidyr::pivot_wider(names_from = rater, values_from = label) %>% dplyr::select(-unit)
mat <- as.matrix(wide)
result <- kripp.alpha(mat, method = "nominal")
print(result)
if (result$value >= 0.80) {
  cat("Reliability: STRONG (>= 0.80)\n")
} else if (result$value >= 0.667) {
  cat("Reliability: TENTATIVE (>= 0.667 and < 0.80)\n")
} else {
  cat("Reliability: INSUFFICIENT (< 0.667)\n")
}

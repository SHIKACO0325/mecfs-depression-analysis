# Manuscript wording and citation — templates, not publication claims

## Before the repository is shared

Working-draft wording:

> The data and analysis notebooks were provided by the author for review. A repository is being prepared; its public availability and the provider's redistribution permission have not yet been established. The dataset's empirical or synthetic nature and label-generation procedures require confirmation.

## After an accessible repository exists

Use only after replacing all bracketed fields and verifying that the statement is true:

> The analysis code and supporting materials are available at [REPOSITORY URL], at [RELEASE OR COMMIT]. The archived original analysis contains the preprocessing limitations described in Section [SECTION].

If data are actually included and authorized for sharing, replace “supporting materials” with “data”. If data are restricted, explain the actual access conditions separately; do not imply the repository provides them.

## Data source is a separate statement

If confirmed synthetic:

> This study conducted a secondary analysis of a synthetic dataset provided by [PROVIDER, WITH PERMISSION]. The data were generated using [DOCUMENTED GENERATION METHOD], and the outcome labels were assigned using [DOCUMENTED LABEL RULES]. The records do not represent observed patients.

Use this only when those facts are confirmed. Do not attribute an official dataset to Coursera solely because the instructor taught a course there.

## Reference-list template

> [VERIFIED CODE AUTHORS]. [YEAR]. ME/CFS and depression: exploratory classification materials. [VERSION OR COMMIT]. GitHub. [REPOSITORY URL]. Accessed [ACTUAL ACCESS DATE].

Repository authorship and original dataset authorship may differ. Confirm both. When publication metadata are available, cite the actual paper separately. No DOI has been created by preparing this repository.

After confirming metadata, copy `CITATION.cff.example` to `CITATION.cff`, complete it, and put it in the repository root. GitHub supports a “Cite this repository” link for a valid citation file:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files

For the final paper, cite a stable release or exact commit rather than relying only on a changing default branch. Uploading files does not establish clinical data provenance or correct model leakage.

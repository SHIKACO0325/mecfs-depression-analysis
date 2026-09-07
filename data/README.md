# Data documentation — unresolved provenance

Both supplied CSV files have 1,620 rows and 16 columns. No exact duplicate rows were found. Observed, nonmissing values match row-by-row between the files. These checks do not establish participant independence or clinical authenticity.

`raw/Data.csv` contains 333 missing cells across 302 rows. `legacy_processed/multiple_imputed.csv` contains no missing values. The latter filename is original: the supplied code produces one iterative-imputation result, not multiple completed datasets with pooled estimates.

## Fields

Nine numerical inputs: `age`, `sleep_quality_index`, `brain_fog_level`, `physical_pain_score`, `stress_level`, `depression_phq9_score`, `fatigue_severity_scale_score`, `pem_duration_hours`, `hours_of_sleep_per_night`.

Six categorical inputs: `gender`, `pem_present`, `work_status`, `social_activity_level`, `exercise_frequency`, `meditation_or_mindfulness`.

Target: `diagnosis`, containing `ME/CFS`, `Depression`, and `Both`.

Field names are not proof of validated instruments. Four observed records report zero sleep hours; 602 have `pem_present = 0` and positive duration, while 16 have `pem_present = 1` and zero duration. Definitions and time frames are needed before deciding whether these combinations require correction. The observed fatigue field ranges from 2 to 10; its instrument remains unconfirmed.

## Information still required from the provider

- Dataset creator, course context, date/version, original filename, and attribution preference.
- Whether the data are empirical, synthetic, or mixed; generation code or collection documentation.
- Rules or clinical procedures establishing each diagnosis label, including any use of input symptoms.
- Full dictionary: units, valid ranges, coding, measurement time frames, and missing-value conventions.
- Permission to use the material in a publication and to redistribute it on GitHub.
- Any applicable original consent/ethics documentation; do not invent approval or exemption claims.

The author has described an instructor connection to Coursera. No official Coursera ownership, endorsement, hosting, or dataset provenance has been verified.

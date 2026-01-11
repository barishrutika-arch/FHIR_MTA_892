# Source to Target Mapping

This document describes how legacy CSV data fields are mapped
to FHIR resource elements.

| Source Field | FHIR Resource | FHIR Element |
|-------------|--------------|--------------|
| patient_id | Patient | Patient.id |
| gender | Patient | Patient.gender |
| birthdate | Patient | Patient.birthDate |
| heart_rate | Observation | Observation.valueQuantity |

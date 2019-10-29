from pymongo import MongoClient
import pandas as pd
import json


client=MongoClient("mongodb+srv://test:1234@cluster0-wytxl.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database('water_quality_uk')

records=db.wq_wessex

new_doc={
    "@id": "http://environment.data.gov.uk/water-quality/data/measurement/SW-3368551-0061",
    "sample.samplingPoint": "http://environment.data.gov.uk/water-quality/id/sampling-point/SW-50010208",
    "sample.samplingPoint.notation": "SW-50010208",
    "sample.samplingPoint.label": "RIVER MUDE AT RAVEN WAY",
    "sample.sampleDateTime": "2019-01-02T09:11:00",
    "determinand.label": "pH",
    "determinand.definition": "pH",
    "determinand.notation": "0061",
    "resultQualifier.notation": "",
    "result": 8.22,
    "codedResultInterpretation.interpretation": "",
    "determinand.unit.label": "phunits",
    "sample.sampledMaterialType.label": "RIVER / RUNNING SURFACE WATER",
    "sample.isComplianceSample": False,
    "sample.purpose.label": "ENVIRONMENTAL MONITORING STATUTORY (EU DIRECTIVES)",
    "sample.samplingPoint.easting": 418208,
    "sample.samplingPoint.northing": 92297
}
records.insert_one(new_doc)


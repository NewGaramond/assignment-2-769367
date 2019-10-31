from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'water_quality_uk'
app.config['MONGO_URI'] = 'mongodb+srv://test:1234@cluster0-wytxl.gcp.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.framework

    output=[]

    for q in framework.find():
        output.append(
            {
                "@id": q["@id"],
                "sample_samplingPoint": q["sample_samplingPoint"],
                "sample_samplingPoint_notation":q["sample_samplingPoint_notation"],
                "sample_samplingPoint_label": q["sample_samplingPoint_label"],
                "sample_sampleDateTime": q["sample_sampleDateTime"],
                "determinand_label": q["determinand_label"],
                "determinand_definition": q["determinand_definition"],
                "determinand_notation": q["determinand_notation"],
                "resultQualifier_notation": q["resultQualifier_notation"],
                "result": q["result"],
                "codedResultInterpretation_interpretation": q["codedResultInterpretation_interpretation"],
                "determinand_unit_label": q["determinand_unit_label"],
                "sample_sampledMaterialType_label": q["sample_sampledMaterialType_label"],
                "sample_isComplianceSample": q["sample_isComplianceSample"],
                "sample_purpose_label": q["sample_purpose_label"],
                "sample_samplingPoint_easting": q["sample_samplingPoint_easting"],
                "sample_samplingPoint_northing": q["sample_samplingPoint_northing"]
            })
    return jsonify({'result' : output})
@app.route('/framework/<label>',methods=['GET'])
def get_one_framework(label):
    framework=mongo.db.framework

    q=framework.find_one({"sample_samplingPoint_label": label})
    output={
                "@id": q["@id"],
                "sample_samplingPoint": q["sample_samplingPoint"],
                "sample_samplingPoint_notation":q["sample_samplingPoint_notation"],
                "sample_samplingPoint_label": q["sample_samplingPoint_label"],
                "sample_sampleDateTime": q["sample_sampleDateTime"],
                "determinand_label": q["determinand_label"],
                "determinand_definition": q["determinand_definition"],
                "determinand_notation": q["determinand_notation"],
                "resultQualifier_notation": q["resultQualifier_notation"],
                "result": q["result"],
                "codedResultInterpretation_interpretation": q["codedResultInterpretation_interpretation"],
                "determinand_unit_label": q["determinand_unit_label"],
                "sample_sampledMaterialType_label": q["sample_sampledMaterialType_label"],
                "sample_isComplianceSample": q["sample_isComplianceSample"],
                "sample_purpose_label": q["sample_purpose_label"],
                "sample_samplingPoint_easting": q["sample_samplingPoint_easting"],
                "sample_samplingPoint_northing": q["sample_samplingPoint_northing"]
            }
    return jsonify({'result': output})
@app.route('/framework', methods=['POST'])
def add_framework():
    framework = mongo.db.framework
    id= request.json["@id"],
    sample_samplingPoint= request.json["sample_samplingPoint"],
    sample_samplingPoint_notation= request.json["sample_samplingPoint_notation"],
    sample_samplingPoint_label= request.json["sample_samplingPoint_label"],
    sample_sampleDateTime= request.json["sample_sampleDateTime"],
    determinand_label= request.json["determinand_label"],
    determinand_definition= request.json["determinand_definition"],
    determinand_notation= request.json["determinand_notation"],
    resultQualifier_notation= request.json["resultQualifier_notation"],
    result= request.json["result"],
    codedResultInterpretation_interpretation= request.json["codedResultInterpretation_interpretation"],
    determinand_unit_label= request.json["determinand_unit_label"],
    sample_sampledMaterialType_label= request.json["sample_sampledMaterialType_label"],
    sample_isComplianceSample= request.json["sample_isComplianceSample"],
    sample_purpose_label= request.json["sample_purpose_label"],
    sample_samplingPoint_easting= request.json["sample_samplingPoint_easting"],
    sample_samplingPoint_northing= request.json["sample_samplingPoint_northing"]
    framework_id = framework.insert({'@id' : id,
                                     "sample_samplingPoint" : sample_samplingPoint,
                                     "sample_samplingPoint_notation":sample_samplingPoint_notation,
                                     "sample_samplingPoint_label":sample_samplingPoint_label,
                                     "sample_sampleDateTime":sample_sampleDateTime,
                                     "determinand_label":determinand_label,
                                     "determinand_definition":determinand_definition,
                                     "determinand_notation":determinand_notation,
                                     "resultQualifier_notation":resultQualifier_notation,
                                     "result":result,
                                     "codedResultInterpretation_interpretation":codedResultInterpretation_interpretation,
                                     "determinand_unit_label":determinand_unit_label,
                                     "sample_sampledMaterialType_label":sample_sampledMaterialType_label,
                                     "sample_isComplianceSample":sample_isComplianceSample,
                                     "sample_purpose_label":sample_purpose_label,
                                     "sample_samplingPoint_easting":sample_samplingPoint_easting,
                                     "sample_samplingPoint_northing":sample_samplingPoint_northing
                                     })
    new_framework = framework.find_one({'_id' : framework_id})

    output = {   "@id" : new_framework["@id"],
                 "sample_samplingPoint" : new_framework["sample_samplingPoint"],
                 "sample_samplingPoint_notation": new_framework["sample_samplingPoint_notation"],
                 "sample_samplingPoint_label": new_framework["sample_samplingPoint_label"],
                 "sample_sampleDateTime": new_framework["sample_sampleDateTime"],
                 "determinand_label": new_framework["determinand_label"],
                 "determinand_definition": new_framework["determinand_definition"],
                 "determinand_notation": new_framework["determinand_notation"],
                 "resultQualifier_notation": new_framework["resultQualifier_notation"],
                 "result": new_framework["result"],
                 "codedResultInterpretation_interpretation": new_framework["codedResultInterpretation_interpretation"],
                 "determinand_unit_label": new_framework["determinand_unit_label"],
                 "sample_sampledMaterialType_label": new_framework["sample_sampledMaterialType_label"],
                 "sample_isComplianceSample": new_framework["sample_isComplianceSample"],
                 "sample_purpose_label": new_framework["sample_purpose_label"],
                 "sample_samplingPoint_easting": new_framework["sample_samplingPoint_easting"],
                 "sample_samplingPoint_northing": new_framework["sample_samplingPoint_northing"],
                                     }

    return jsonify({'result' : output})
if __name__ == '__main__':
    app.run(debug=True)
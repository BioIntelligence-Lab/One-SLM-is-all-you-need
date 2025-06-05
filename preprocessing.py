import json

def preprocess_function_harmonize_series(example,i):
    instruction = 'Harmonize sequence name.'
    id=example['index_col'][i]
    with open("../harmonize_series/"+str(id)+".json") as f:
        d = json.load(f)
    d_str=str(d)
    text = f"### Instruction:\n{instruction}\n\n### Input:\n{list(d.keys())[0]}\n\n### Response: \n {d}</s>\n"
    return text


def preprocess_function_response(example,i):
    accid=example['ACCID'][i]
    with open("../response/"+str(accid)+".json") as f:
        d = json.load(f)
    d=str(d)
    text = f"### Instruction:\nReport CXR diagnosis.\n\n### Input:\n{example['REPORT'][i]}\n\n### Response: \n {d}</s>\n"
    return text

def preprocess_function_impression(example,i):
    t=example['REPORT'][i]
    findings=t.split('IMPRESSION')[0][:-2]
    impression='IMPRESSION '+t.split('IMPRESSION')[1]
    text = f"### Instruction:\nGenerate radiology report based on the following text.\n\n### Input:\n{findings}\n\n### Response: \n {impression}</s>\n"
    return text

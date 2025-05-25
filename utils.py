def filter_ner_io(sentence, tagset):
    result=[['O']]*len(sentence['tokens'])
    for span in sentence['spans']:
        if(span['label'] in tagset):
            add=True
            if(span['label'].startswith('ENE-')):
                for s in sentence['spans']:
                    if s["label"].startswith("ENE-"):
                        if((span['start']<s['start'] and s['end']<=span['end']) or (span['start']<=s['start'] and s['end']<span['end'])):
                            add=False
            if(add):
                for i in range(span['token_start'],span['token_end']+1):
                    if(result[i]==['O']):
                        result[i]=[span['label']]
                    else:
                        result[i].append(span['label'])
                        result[i]=sorted(result[i])

    return result
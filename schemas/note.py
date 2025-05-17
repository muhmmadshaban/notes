def noteConvertor(item)-> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "des": item["des"],
        "importance": item["importance"] 
    }

def noteEntity(items)-> list:
    return [noteConvertor(item) for item in items]
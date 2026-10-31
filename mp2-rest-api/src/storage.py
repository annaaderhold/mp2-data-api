import logging
logger = logging.getLogger(__name__)

class DatasetStorage:
    def __init__(self):
        self._store = {}
        self._counter = 0
    
    def save(self, df, filename):
        self._counter += 1
        dataset_id = self._counter
        self._store[dataset_id] = {
            "filename": filename,
            "df": df.copy(),
        }
        logger.debug(f"Stored dataset: id={dataset_id}, rows={len(df)}")
        return dataset_id

    def get(self, dataset_id):
        entry = self._store.get(dataset_id)
        if entry is None:
            logger.debug(f"Dataset not found in storage: id={dataset_id}")
            return None
        df = entry["df"].copy()
        logger.debug(f"Retrieved dataset copy: id={dataset_id}")
        return df
    

    def get_metadata(self, dataset_id):
        entry = self._store.get(dataset_id)
        if entry is None:
            return None
        df = entry["df"]
        return {
            "id": dataset_id,
            "filename": entry["filename"],
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": [str(c) for c in df.columns],
        }
    
    def update(self, dataset_id, df):
        if dataset_id not in self._store:
            logger.debug(f"Cannot update missing dataset: id={dataset_id}")
            return False
        self._store[dataset_id]["df"] = df.copy()
        logger.debug(f"Updated dataset: id={dataset_id}, rows={len(df)}")
        return True

    def clear(self):
        self._store.clear()
        self._counter = 0
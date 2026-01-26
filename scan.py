from spiral import Spiral
import tqdm

sp = Spiral(overrides={
    "manifests_cache.enabled": "1",
    "manifests_cache.memory_capacity_bytes": "0",
    "manifests_cache.disk_capacity_bytes": "1073741824",  # 1GiB
})
project = sp.project("enigma-spiral-poc-2-724186")
tbl_vjepa_embeddings = project.table("vjepa_embeddings")

vjepa_embeddings_scan = sp.scan(tbl_vjepa_embeddings["tensor"], where=tbl_vjepa_embeddings["layer"] == 4)

for batch in tqdm.tqdm(vjepa_embeddings_scan.to_record_batches(batch_readahead=32, hide_progress_bar=True)):
    pass

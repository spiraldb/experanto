from spiral import Spiral
import tqdm

sp = Spiral()
project = sp.project("enigma-spiral-poc-2-724186")
tbl_vjepa_embeddings = project.table("vjepa_embeddings")

vjepa_embeddings_scan = sp.scan(tbl_vjepa_embeddings["tensor"], where=tbl_vjepa_embeddings["layer"] == 4)

for batch in tqdm.tqdm(vjepa_embeddings_scan.to_record_batches()):
    pass

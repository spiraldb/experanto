from spiral import Spiral
import time

sp = Spiral(overrides={
    # "manifests_cache.enabled": "1",
    # "manifests_cache.memory_capacity_bytes": "0",
    # "manifests_cache.disk_capacity_bytes": "1073741824",  # 1GiB
})
project = sp.project("public-177331")  # Spiral project
table = project.table("enigma-embeddings-v3")

# Do not time opening a scan.
scan = sp.scan(table[["embeddings"]])  # full table scan
# scan = sp.scan(table[["embeddings"]], where=(table["session"] == f"very_long_session_identifier_0") & (table["layer"] == 0))

st = time.time()
num_rows = 0
for batch in scan.to_record_batches():
    num_rows += batch.num_rows
et = time.time()

# NOTE(marko): This is an example of suboptimal layout for embeddings.
#   Needs to scan 9 ~110MBs files, only to get ~135MBs of embeddings.
print(
    f"Scanned session/layer 0 in {et - st:.2f} seconds; "
    f"got {num_rows} rows / {float(num_rows * 1408 * 4) / (1024 * 1024)} MBs"
)
scan._dump_metrics()

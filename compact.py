from spiral import Spiral

sp = Spiral()
project = sp.project("enigma-spiral-poc-2-724186")
tbl_vidtok_embeddings = project.table("vidtok_embeddings")

with tbl_vidtok_embeddings.txn() as txn:
    txn.compact_column_group("table_4cpkjo.tensor")

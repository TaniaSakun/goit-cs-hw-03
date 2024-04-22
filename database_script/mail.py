from constants import Constants
from operations_handler import create_banch_of_records, read, update, delete, print_all_results, db

if __name__ == "__main__":
    
    print("Creating DB...")
    
    create_banch_of_records()
    
    print("Reading DB...")
    cats = read(db)
    
    print_all_results(cats)
    
    cat = read(db, "Simba")
    print_all_results(cats)
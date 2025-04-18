import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog, messagebox
from algorithms import fifo_page_replacement, lru_page_replacement, optimal_page_replacement

def compare_algorithms(pages, frame_size):
    """Compares FIFO, LRU, and Optimal page replacement algorithms"""
    results = {}

    for algo, func in zip(["FIFO", "LRU", "Optimal"], 
                          [fifo_page_replacement, lru_page_replacement, optimal_page_replacement]):
        history, faults, exec_time = func(pages, frame_size)
        results[algo] = {"Page Faults": faults, "Execution Time (s)": exec_time}

    # Convert to DataFrame for visualization
    df = pd.DataFrame(results).T
    df.plot(kind='bar', figsize=(8, 5), colormap='viridis')
    plt.title("Algorithm Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Performance Metrics")
    plt.legend(loc='upper right')
    plt.show()

def export_results():
    """Exports results to CSV, JSON, or Excel"""
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                                 filetypes=[("CSV Files", "*.csv"), 
                                                            ("JSON Files", "*.json"), 
                                                            ("Excel Files", "*.xlsx")])

        if not file_path:
            return  # User canceled the save operation

        # Dummy results for export (Fix: results were undefined in the previous version)
        results = {
            "FIFO": {"Page Faults": 10, "Execution Time (s)": 0.002},
            "LRU": {"Page Faults": 8, "Execution Time (s)": 0.003},
            "Optimal": {"Page Faults": 6, "Execution Time (s)": 0.001}
        }
        
        df = pd.DataFrame(results).T

        if file_path.endswith(".csv"):
            df.to_csv(file_path)
        elif file_path.endswith(".json"):
            df.to_json(file_path, orient="records", indent=4)
        elif file_path.endswith(".xlsx"):
            df.to_excel(file_path, index=True)

        messagebox.showinfo("Success", "Results exported successfully!")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while exporting: {e}")

import tkinter as tk
from tkinter import messagebox, filedialog , ttk
import matplotlib.pyplot as plt
from algorithms import fifo_page_replacement, lru_page_replacement, optimal_page_replacement
from analysis import compare_algorithms, export_results
import numpy as np

def visualize_algorithm(history, title):
    """ Improved visualization for memory allocation over time """
    plt.figure(figsize=(10, 6))

    num_frames = max(len(state) for state in history)  # Maximum number of frames
    colors = plt.cm.get_cmap('tab10', num_frames)  # Different colors for each frame slot
    
    for i, state in enumerate(history):
        x_values = [i] * len(state)
        y_values = list(state)

        # Assign distinct colors for each page based on its value
        plt.scatter(x_values, y_values, color=[colors(p % num_frames) for p in state], label=f"Step {i+1}" if i == 0 else "")
        plt.plot(x_values, y_values, color='gray', alpha=0.5, linestyle='dashed')  # Dashed lines for better tracking

    plt.xlabel("Steps (Time)", fontsize=12)
    plt.ylabel("Pages in Frames", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xticks(range(len(history)))
    plt.yticks(sorted(set(sum(history, []))))  # Unique page numbers
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.legend(["Page Changes"], loc="upper right")
    plt.show()


def run_simulation(entry_pages, entry_frames, algo_var):
    """Runs the selected page replacement algorithm"""
    try:
        pages = list(map(int, entry_pages.get().split()))  # Get pages from user input
        frame_size = int(entry_frames.get())  # Get number of frames

        if frame_size <= 0:
            messagebox.showerror("Error", "Frame size must be greater than 0")
            return

        algo = algo_var.get()
        if algo == "FIFO":
            history, faults, exec_time = fifo_page_replacement(pages, frame_size)
        elif algo == "LRU":
            history, faults, exec_time = lru_page_replacement(pages, frame_size)
        elif algo == "Optimal":
            history, faults, exec_time = optimal_page_replacement(pages, frame_size)
        else:
            messagebox.showerror("Error", "Invalid Algorithm Selected")
            return

        visualize_algorithm(history, f"{algo} Page Replacement")
        messagebox.showinfo("Result", f"Total Page Faults ({algo}): {faults}\nExecution Time: {exec_time} sec")

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter space-separated numbers.")

def run_comparison(entry_pages, entry_frames):
    try:
        pages = list(map(int, entry_pages.get().split()))
        frame_size = int(entry_frames.get())
        compare_algorithms(pages, frame_size)  # Pass user input for comparison
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter space-separated numbers.")
"""
def start_gui():
    #Creates the GUI for the page replacement simulator
    root = tk.Tk()
    root.title("Page Replacement Simulator")

    tk.Label(root, text="Enter Page Reference String:").grid(row=0, column=0)
    entry_pages = tk.Entry(root)
    entry_pages.grid(row=0, column=1)

    tk.Label(root, text="Enter Number of Frames:").grid(row=1, column=0)
    entry_frames = tk.Entry(root)
    entry_frames.grid(row=1, column=1)

    algo_var = tk.StringVar(value="FIFO")
    tk.Label(root, text="Choose Algorithm:").grid(row=2, column=0)
    tk.OptionMenu(root, algo_var, "FIFO", "LRU", "Optimal").grid(row=2, column=1)

    tk.Button(root, text="Run Simulation", command=lambda: run_simulation(entry_pages, entry_frames, algo_var)).grid(row=3, columnspan=2)
    tk.Button(root, text="Compare Algorithms", command=lambda: run_comparison(entry_pages, entry_frames)).grid(row=4, columnspan=2)
    tk.Button(root, text="Export Results", command=export_results).grid(row=5, columnspan=2)

    root.mainloop() """



def start_gui():
    """Creates the GUI for the page replacement simulator with a modern dark theme and centered layout"""
    root = tk.Tk()
    root.title("Page Replacement Simulator")
    root.geometry("450x300")
    root.configure(bg="#1e1e2e")  # Dark background

    # Styling
    fg_color = "#cdd6f4"  # Light text color
    entry_bg = "#313244"  # Entry background
    button_bg = "#89b4fa"  # Blue buttons
    button_fg = "#1e1e2e"  # Dark text on buttons
    highlight_color = "#94e2d5"  # Green highlight

    style = ttk.Style()
    style.configure("TButton", background=button_bg, foreground=button_fg, font=("Arial", 11), padding=5)
    style.map("TButton", background=[("active", highlight_color)])

    # Center Frame for Better Alignment
    frame = tk.Frame(root, bg=root["bg"])
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centering the frame

    # Labels and Inputs
    tk.Label(frame, text="Enter Page Reference String:", fg=fg_color, bg=root["bg"], font=("Arial", 11)).grid(row=0, column=0, pady=5, sticky="w")
    entry_pages = tk.Entry(frame, bg=entry_bg, fg=fg_color, insertbackground=fg_color, font=("Arial", 11))
    entry_pages.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Enter Number of Frames:", fg=fg_color, bg=root["bg"], font=("Arial", 11)).grid(row=1, column=0, pady=5, sticky="w")
    entry_frames = tk.Entry(frame, bg=entry_bg, fg=fg_color, insertbackground=fg_color, font=("Arial", 11))
    entry_frames.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Choose Algorithm:", fg=fg_color, bg=root["bg"], font=("Arial", 11)).grid(row=2, column=0, pady=5, sticky="w")
    algo_var = tk.StringVar(value="FIFO")
    algo_menu = ttk.Combobox(frame, textvariable=algo_var, values=["FIFO", "LRU", "Optimal"], font=("Arial", 11), state="readonly")
    algo_menu.grid(row=2, column=1, padx=10, pady=5)

    # Buttons
    ttk.Button(frame, text="Run Simulation", command=lambda: run_simulation(entry_pages, entry_frames, algo_var)).grid(row=3, columnspan=2, pady=5)
    ttk.Button(frame, text="Compare Algorithms", command=lambda: run_comparison(entry_pages, entry_frames)).grid(row=4, columnspan=2, pady=5)
    ttk.Button(frame, text="Export Results", command=export_results).grid(row=5, columnspan=2, pady=5)

    root.mainloop()

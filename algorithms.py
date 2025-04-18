import time

def fifo_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0
    history = []
    start_time = time.time()
    
    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)  # Remove the oldest page
                frames.append(page)
            page_faults += 1
        history.append(list(frames))  # Track frame state at each step
    
    exec_time = round(time.time() - start_time, 5)
    return history, page_faults, exec_time

def lru_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0
    history = []
    start_time = time.time()
    
    for page in pages:
        if page in frames:
            frames.remove(page)  # Move page to the end (most recently used)
        else:
            if len(frames) >= frame_size:
                frames.pop(0)  # Remove least recently used page
                page_faults += 1
            page_faults += 1  # Page fault occurs if the page was not in memory
        frames.append(page)
        history.append(list(frames))
    
    exec_time = round(time.time() - start_time, 5)
    return history, page_faults, exec_time

def optimal_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0
    history = []
    start_time = time.time()
    
    for i in range(len(pages)):
        page = pages[i]
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Find the page in memory that will be used farthest in the future
                future_use = {f: pages[i+1:].index(f) if f in pages[i+1:] else float('inf') for f in frames}
                victim = max(future_use, key=future_use.get)  # Select the farthest used page
                frames.remove(victim)
                frames.append(page)
            page_faults += 1
        history.append(list(frames))
    
    exec_time = round(time.time() - start_time, 5)
    return history, page_faults, exec_time

import tkinter as tk

class TaskManagerApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Attention Boost")
    self.tasks = []
    self.create_widgets()

  def create_widgets(self):
    self.title_label = tk.Label(self, text="Attention Boost", font=("Helvetica", 16),bg="#F7DDC8")
    self.title_label.pack(side="top", fill="x")

    # Create the task entry field and "Add" button
    self.task_entry = tk.Entry(self, width=50)
    self.task_entry.pack(side="top", padx=5, pady=5)
    tk.Button(self, text="Add", command=self.add_task,activebackground="#73DFF7",bg="#F9AD6D",fg="#8B5427",activeforeground="#156798").pack(side="top", padx=5, pady=5)

    # Create the task list frame and scrollbar
    list_frame = tk.Frame(self)
    list_frame.pack(side="left", fill="both", expand=True)
    tk.Scrollbar(list_frame, orient="vertical").pack(side="right", fill="y")
    self.task_list = tk.Listbox(list_frame, selectmode="single", width=50)
    self.task_list.pack(side="left", fill="both", expand=True)
    self.refresh_task_list()

    # Create the task control frame and buttons
    control_frame = tk.Frame(self,bg="#F7DDC8")
    control_frame.pack(side="right", padx=5, pady=5)
    tk.Button(control_frame, text="Complete", command=self.complete_task,activebackground="#73DFF7",bg="#F9AD6D",fg="#8B5427",activeforeground="#156798").pack(side="top", padx=5, pady=5)
    tk.Button(control_frame, text="Quit", command=self.quit,activebackground="#73DFF7",bg="#F9AD6D",fg="#8B5427",activeforeground="#156798").pack(side="top", padx=5, pady=5)

  def add_task(self):
    task = self.task_entry.get()
    self.tasks.append(task)
    self.task_entry.delete(0, "end")
    self.refresh_task_list()

  def complete_task(self):
    task_index = self.task_list.curselection()[0]
    del self.tasks[task_index]
    self.refresh_task_list()

  def refresh_task_list(self):
    self.task_list.delete(0, "end")
    for task in self.tasks:
      self.task_list.insert("end", task)

app = TaskManagerApp()
app.configure(bg="#F7DDC8")
app.mainloop()

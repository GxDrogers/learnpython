import ttkbootstrap as tb
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import subprocess
import threading
import re

class PythonTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Text Editor")
        self.root.geometry("1100x650")
        tb.Style("cyborg")  # Changed theme to 'cyborg' for a more modern look
        
        # Main Layout Frames
        self.main_frame = tb.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button Frame (Moved to Top Left)
        self.button_frame = tb.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=5, anchor="w")
        
        self.run_button = tb.Button(self.button_frame, text="▶ Run", command=self.run_code, bootstyle="success-outline")
        self.run_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tb.Button(self.button_frame, text="🗑 Clear Output", command=self.clear_output, bootstyle="danger-outline")
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.open_button = tb.Button(self.button_frame, text="📂 Open File", command=self.open_file, bootstyle="primary-outline")
        self.open_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = tb.Button(self.button_frame, text="💾 Save File", command=self.save_file, bootstyle="info-outline")
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        # Editor & Output Frame
        self.editor_output_frame = tb.Frame(self.main_frame)
        self.editor_output_frame.pack(fill=tk.BOTH, expand=True)
        
        # Code Editor Frame
        self.editor_frame = tb.LabelFrame(self.editor_output_frame, text="Code Editor", padding=10, bootstyle="dark")
        self.editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.text_editor = scrolledtext.ScrolledText(
            self.editor_frame, wrap=tk.WORD, font=("Fira Code", 14), undo=True, height=20, width=60,
            bg="#1b1b1b", fg="#d4d4d4", insertbackground="white", borderwidth=0
        )
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        self.text_editor.bind("<KeyRelease>", self.highlight_syntax)
        
        # Output Frame
        self.output_frame = tb.LabelFrame(self.editor_output_frame, text="Output", padding=10, bootstyle="dark")
        self.output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.output_box = scrolledtext.ScrolledText(
            self.output_frame, wrap=tk.WORD, font=("Fira Code", 12), height=10, width=50,
            bg="#242424", fg="#d4d4d4", state=tk.DISABLED, borderwidth=0
        )
        self.output_box.pack(fill=tk.BOTH, expand=True)
    
    def highlight_syntax(self, event=None):
        keywords = ["def", "class", "import", "from", "as", "return", "if", "elif", "else", "try", "except", "for", "while", "with"]
        operators = ["=", "+", "-", "*", "/", "%", "!", "<", ">", "&", "|"]
        CREATER = ["MIDHUN", "midhun", "M", "Mitz", "mitz", "m"]
        self.text_editor.tag_remove("keyword", "1.0", tk.END)
        self.text_editor.tag_remove("operator", "1.0", tk.END)
        self.text_editor.tag_remove("CREATER", "1.0", tk.END)

        
        text = self.text_editor.get("1.0", tk.END)
        for word in keywords:
            for match in re.finditer(rf"\b{word}\b", text):
                self.text_editor.tag_add("keyword", f"1.{match.start()}", f"1.{match.end()}")
        
        for op in operators:
            for match in re.finditer(re.escape(op), text):
                self.text_editor.tag_add("operator", f"1.{match.start()}", f"1.{match.end()}")

        for c in CREATER:
            for match in re.finditer(re.escape(c), text):
                self.text_editor.tag_add("CREATER", f"1.{match.start()}", f"1.{match.end()}")
        
        self.text_editor.tag_config("keyword", foreground="#FFCC00")
        self.text_editor.tag_config("operator", foreground="#FF6666")
        self.text_editor.tag_config("CREATER", foreground="#68A2DB")
    
    def run_code(self):
        code = self.text_editor.get("1.0", tk.END)
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete("1.0", tk.END)
        self.output_box.config(state=tk.DISABLED)
        
        def execute():
            try:
                result = subprocess.run(
                    ["python", "-c", code], capture_output=True, text=True, timeout=5
                )
                output = result.stdout if result.stdout else result.stderr
            except Exception as e:
                output = str(e)

            self.output_box.config(state=tk.NORMAL)
            self.output_box.insert(tk.END, output)
            self.output_box.config(state=tk.DISABLED)
        
        threading.Thread(target=execute, daemon=True).start()
    
    def clear_output(self):
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete("1.0", tk.END)
        self.output_box.config(state=tk.DISABLED)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert("1.0", content)
                self.highlight_syntax()
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_editor.get("1.0", tk.END))
            messagebox.showinfo("Success", "File Saved Successfully!")

if __name__ == "__main__":
    root = tb.Window(themename="cyborg")  # Changed theme to 'cyborg'
    tb.Style("cyborg")
    app = PythonTextEditor(root)
    root.mainloop()

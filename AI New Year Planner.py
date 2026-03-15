import tkinter as tk
from tkinter import messagebox

# ---------------- AI Logic ----------------
def generate_plan():
    goal = goal_entry.get()
    hours = int(hours_entry.get())
    category = category_var.get()

    if not goal:
        messagebox.showerror("Error", "Please enter a goal")
        return

    # -------- Rule-Based AI --------
    if category == "Study":
        monthly = "Learn fundamentals → practice → projects"
        strategy = "Pomodoro Technique"
    else:
        monthly = "Skill building → productivity → optimization"
        strategy = "Time Blocking"

    if hours < 2:
        advice = "Use micro-tasks (25 min sessions)"
    elif hours <= 4:
        advice = "Use deep focus blocks (90 min)"
    else:
        advice = "Balance work & rest to avoid burnout"

    weekly_hours = hours * 7

    # -------- Output --------
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"🎯 GOAL: {goal}\n\n")
    output.insert(tk.END, "📅 YEAR PLAN:\n")
    output.insert(tk.END, f"- {monthly}\n\n")
    output.insert(tk.END, "🗓️ WEEKLY PLAN:\n")
    output.insert(tk.END, f"- Study/Work Hours per Week: {weekly_hours}\n\n")
    output.insert(tk.END, "⏰ TIME MANAGEMENT STRATEGY:\n")
    output.insert(tk.END, f"- {strategy}\n")
    output.insert(tk.END, f"- {advice}\n\n")
    output.insert(tk.END, "✅ AI Recommendation:\n")
    output.insert(tk.END, "Stay consistent. Review progress monthly.")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("🧠 AI-Powered New Year Planner")
root.geometry("600x500")

tk.Label(root, text="AI New Year Planner", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Enter Your Goal:").pack()
goal_entry = tk.Entry(root, width=40)
goal_entry.pack(pady=5)

tk.Label(root, text="Hours Available per Day:").pack()
hours_entry = tk.Entry(root, width=10)
hours_entry.pack(pady=5)

tk.Label(root, text="Goal Category:").pack()
category_var = tk.StringVar(value="Study")
tk.OptionMenu(root, category_var, "Study", "Work").pack()

tk.Button(root, text="Generate AI Plan", command=generate_plan).pack(pady=15)

output = tk.Text(root, height=15, width=70)
output.pack()

root.mainloop()

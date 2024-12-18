import math
import tkinter as tk
from tkinter import simpledialog, messagebox
from rdflib import Graph

# Functions to explain shape properties and calculations
def explain_circle():
    return (
        "Circle Area Calculation:\n"
        "1. A circle is a shape with all points equidistant from its center.\n"
        "2. The formula for the area of a circle is: Area = π × radius²\n"
        "3. 'π' (pi) is approximately 3.14159.\n"
    )

def explain_rectangle():
    return (
        "Rectangle Area Calculation:\n"
        "1. A rectangle is a shape with opposite sides equal and all angles 90°.\n"
        "2. The formula for the area of a rectangle is: Area = base × height\n"
    )

def explain_triangle():
    return (
        "Triangle Area Calculation:\n"
        "1. A triangle is a shape with three sides.\n"
        "2. The formula for the area of a triangle is: Area = 0.5 × base × height\n"
    )

# Guided example generator
def guided_example(shape):
    examples = {
        "circle": (
            "Example: Calculating the area of a circle with a radius of 5 units.\n"
            "Step 1: Write the formula: Area = π × radius²\n"
            "Step 2: Substitute the value of radius: Area = π × 5²\n"
            "Step 3: Calculate: Area = π × 25 ≈ 78.54\n"
            "The area of the circle is approximately 78.54 square units.\n"
        ),
        "rectangle": (
            "Example: Calculating the area of a rectangle with a base of 8 units and height of 4 units.\n"
            "Step 1: Write the formula: Area = base × height\n"
            "Step 2: Substitute the values: Area = 8 × 4\n"
            "Step 3: Calculate: Area = 32\n"
            "The area of the rectangle is 32 square units.\n"
        ),
        "triangle": (
            "Example: Calculating the area of a triangle with a base of 6 units and height of 3 units.\n"
            "Step 1: Write the formula: Area = 0.5 × base × height\n"
            "Step 2: Substitute the values: Area = 0.5 × 6 × 3\n"
            "Step 3: Calculate: Area = 9\n"
            "The area of the triangle is 9 square units.\n"
        )
    }
    return examples.get(shape, "No example available for the selected shape.")

# Practice question and validation
def practice_question(shape):
    questions = {
        "circle": ("Calculate the area of a circle with a radius of 7 units.", math.pi * 7**2),
        "rectangle": ("Calculate the area of a rectangle with a base of 10 units and height of 5 units.", 10 * 5),
        "triangle": ("Calculate the area of a triangle with a base of 12 units and height of 8 units.", 0.5 * 12 * 8)
    }
    
    if shape in questions:
        question_text, correct_answer = questions[shape]
        user_answer = simpledialog.askfloat("Practice Question", question_text)
        
        if user_answer is not None:
            if abs(user_answer - correct_answer) < 0.1:
                messagebox.showinfo("Result", "Correct! Well done.")
            else:
                messagebox.showerror("Result", f"Incorrect. The correct answer is approximately {correct_answer:.2f}.")
        else:
            messagebox.showwarning("Input Required", "Please provide an answer.")
    else:
        messagebox.showerror("Error", "Invalid shape for a practice question.")

# Load and display ontology data
def load_ontology(owl_file):
    graph = Graph()
    graph.parse(owl_file, format="xml")
    classes = [str(cls) for cls in graph.subjects()]
    return classes

# Main application logic
def main():
    root = tk.Tk()
    root.title("Geometry Intelligent Tutoring System")
    root.geometry("500x400")

    # Shape selection handler
    def on_select_shape():
        choice = shape_var.get()
        explanations = {
            "circle": explain_circle,
            "rectangle": explain_rectangle,
            "triangle": explain_triangle
        }
        if choice in explanations:
            messagebox.showinfo("Explanation", explanations[choice]())
            messagebox.showinfo("Guided Example", guided_example(choice))
            practice_question(choice)
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid shape.")

    # UI elements
    shape_var = tk.StringVar(value="Select Shape")
    tk.Label(root, text="Select a Shape to Learn:", font=("Arial", 14)).pack(pady=10)
    tk.OptionMenu(root, shape_var, "circle", "rectangle", "triangle").pack(pady=10)

    tk.Button(root, text="Learn", font=("Arial", 12), fg="white", bg="blue", command=on_select_shape).pack(pady=20)

    # Load ontology and display classes
    owl_file = 'IntelligentTutoringSystem.owl'
    ontology_classes = load_ontology(owl_file)
    tk.Button(
        root, 
        text="Show Ontology Classes", 
        font=("Arial", 12), 
        fg="white", 
        bg="green", 
        command=lambda: messagebox.showinfo("Ontology Classes", f"Classes in Ontology:\n{', '.join(ontology_classes)}")
    ).pack(pady=20)

    tk.Button(root, text="Exit", font=("Arial", 12), fg="white", bg="red", command=root.destroy).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()

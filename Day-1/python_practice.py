# Day 1: Python Practice - Basic Concepts

# 1. Variables and Data Types
name = "Kirpya"
age = 21
cgpa = 8.9
is_learning = True

print(f"Name: {name}, Age: {age}, CGPA: {cgpa}")

# 2. Lists
topics = ["AI", "Machine Learning", "Deep Learning", "GenAI"]
print(f"Learning topics: {topics}")

# 3. Dictionaries
student_info = {
    "name": "Kirpya",
    "branch": "CSE-AI",
    "semester": 6,
    "interested_in": "Generative AI"
}

for key, value in student_info.items():
    print(f"{key}: {value}")

# 4. Functions
def greet_student(name, interest):
    return f"Hello {name}! You're interested in {interest}."

print(greet_student("Kirpya", "Generative AI"))

# 5. Loops
print("\nTopics to learn:")
for i, topic in enumerate(topics, 1):
    print(f"{i}. {topic}")

# 6. Classes (Basic OOP)
class AIStudent:
    def __init__(self, name, interest):
        self.name = name
        self.interest = interest
    
    def display_info(self):
        print(f"{self.name} is learning {self.interest}")

student1 = AIStudent("Kirpya", "LLMs and Transformers")
student1.display_info()

print("\n✅ Learning Day 1 Complete!")
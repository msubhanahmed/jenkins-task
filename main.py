class MLOpsClass:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, count):
        if count < 0:
            raise ValueError("Enter number of students : ")
            print("Value cannot be negative ! ")
        self.total_strength += count
        
    def dropStudents(self, count):
        if count < 0:
            raise ValueError("Number of students to drop must be non-negative.")
        if count > self.total_strength:
            raise ValueError("Cannot drop more students than enrolled.")
        self.total_strength -= count
        
    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name

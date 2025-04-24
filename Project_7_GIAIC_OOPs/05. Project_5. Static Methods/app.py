class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


if __name__ == "__main__":
    result = MathUtils.add(5, 3)
    print(f"5 + 3 = {result}")
    
    math = MathUtils()
    result2 = math.add(10, 20)
    print(f"10 + 20 = {result2}") 
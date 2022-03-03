
# by yabeye github
# checkout: https://github.com/yabeye

def main():
    import generator
    g = generator.Generator()
    g.generate_all_combs([])
    print("All possible android patterns are generated, Check out 'all_patterns.txt' file in main.py file's directory.")


if __name__ == "__main__":
    main()


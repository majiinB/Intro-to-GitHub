def main():
	name = input("Enter your name: ")
	if name.strip():
		print(f"Hello, {name}!")
	else:
		print("Hello!")


if __name__ == "__main__":
	main()
#!/bin/python3

# Some functions to help with solving panda exercises

def write_results_str(exercise, result_objects):
	result_path = "ex" + exercise + "-result.txt"
	with open(result_path, "w") as result_file:
		for object in result_objects:		
			result_file.write(str(object))
			result_file.write("\n")

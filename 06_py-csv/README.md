<h3>Liesel Wong (Untitled - Jonathan W., Liesel W.)  </h3>
<h3>SoftDev  </h3>
<h3>K06 -- Explaining K06 python code  </h3>
<h3>2021-09-29  </h3>

---

* __File (CSV) I/0:__ 
  * The program takes a .csv file from GitHub by downloading it from using a RAW url link. Then the program decodes it from 'UTF-8' 
  (which is a standard encoding. Encoding standards tell the web browser  how to interpret the text characters in your HTML or the body of the email for the 
  internet). The decoded text is then turned from stored text in memory and into a data structure for the program to use.
  
* __Dictionary: What is it good for? How does one use?__
  * A dictionary is a data structure (way of storing information). Specifically, the dictionary in python involves a key-value pair. Each key has a value. 
  When you reference a key, you can find the value associated with it (think of it like a key to a door). The first step to use a dictionary is by creating the 
  structure (dictonaryName = {}). To assign values, you type dictionaryName[assignmentKey] = [someValue]. In order to use a dictionary, you could access
  it by referencing it with a specific key. Dictionaries are important because they are easier to traverse than a traditional list structure
  
* __List:__
  * A list is an array of values. To create a list you type listName = ["value","value","value"...]. This data structure allows you to store multiple values in
  the same place. However, you are only allowed to store one type of data structure. A list including Strings must be completely made up of Strings. 

* __Github-Flavored Markdown:__
  * Learning the GitHub-flavored markdown is essential for formatting and writing your files in a way that's easy to read and looks good. For the complete
  basics of all-you-can-learn GitHub-flavored markdown, you can visit [here](https://gist.github.com/cuonggt/9b7d08a597b167299f0d). 
  
* __Weighted Randomized Selection:__
  * Example: I studied for a test, but I didn't study too well for it. I have a 60% chance of passing and a 40% chance of failing. I write a program that randomly 
  picks the outcome of my test. Since the each ending result (pass/fail) has a different chance of happening, this is called weighted randomized selection. 
  In our program, we this process to weigh our job occupations based on a given percentage. To do so, we take the percent, multiply it by 10, 
  add it to itself, and then add that value to a list. Based on the random integer generated, our program compares the cumulative value to the random integer.
  If the random integer is less than the cumulative value, then the program returns the last occupation at a certain index it generated.



# QUESTION 5:MEDRINE link 
#https://www.codewars.com/kata/583203e6eb35d7980400002a/python
# DESCRIPTION:
# Given an array (arr) as an argument complete the function countSmileys that should 
# return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
# Note
# In case of an empty array return 0. You will not be tested with invalid input
# (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
def count_smileys(arr):
    smiley_faces_count = 0

    eyes = [":", ";"]
    noses = ["-", "~"]  #optional
    mouthes = [")", "D"]

    for face in arr:
        if (len(face) == 2 or len(face) == 3) and face[0] in eyes and face[-1] in mouthes: 
            if len(face) == 3 and face[1] in noses:
                smiley_faces_count += 1
            elif len(face) == 2:
                smiley_faces_count += 1

    return smiley_faces_count

print(count_smileys([':)', ';(', ';}', ':-D']))  #2
print(count_smileys([';D', ':-(', ':-)', ';~)'])) #3
print(count_smileys([":)", ";D", ":-)", ":~D", ";-D"])) #5
print(count_smileys([';]', ':[', ';*', ':$', ';-D'])) #1
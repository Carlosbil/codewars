/**Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
 * The first word within the output should be capitalized only if the original word was capitalized 
 * (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior" */

import java.lang.StringBuilder;
class Solution{

  static String toCamelCase(String s){
    
    char[] letters = s.toCharArray();
    boolean cap = false;

    for(int x = 0; x<letters.length;x++){
      if(letters[x]!='-' && letters[x]!='_'){
        if(cap == true){
          letters[x] = Character.toUpperCase(letters[x]);
          cap=false;
        }
      }else{
        cap=true;
      }
    }
    return String.valueOf(letters).replaceAll("[-,_]", "");
  }
}

/**
 * Version pro:
 * static String toCamelCase(String str){
    String[] words = str.split("[-_]");
    return Arrays.stream(words, 1, words.length)
            .map(s -> s.substring(0, 1).toUpperCase() + s.substring(1))
            .reduce(words[0], String::concat);
  }
 */
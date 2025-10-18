public class Solution {
 public bool IsValid(string s)
{
    Stack<char> myStack = new Stack<char>();

    foreach (char c in s)
    {
        if (c == '(' || c == '{' || c == '[')
        {
            myStack.Push(c);
        }
        else
        {
            if (myStack.Count == 0)
                return false;

            char poppedElement = myStack.Pop();

            if (c == ')' && poppedElement != '(')
                return false;
            if (c == '}' && poppedElement != '{')
                return false;
            if (c == ']' && poppedElement != '[')
                return false;
        }
    }

    return myStack.Count == 0;
}


}

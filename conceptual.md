### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
 * Python
 * Javascript
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
 * dict['c']
- What is a unit test?
 * Ensures that a single function works properly and returns the desired output
- What is an integration test?
 * Ensures that multiple functions work together as desired
- What is the role of web application framework, like Flask?
 * 
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
 * A parameter in a route URL is best for passing info as a main category for the page that you're looking for
 * A URL query param is best for passing additional info that simply adds to the page that you're looking for
- How do you collect data from a URL placeholder parameter using Flask?
 * response.get()
- How do you collect data from the query string using Flask?
 * response.args()
- How do you collect data from the body of the request using Flask?
 * response.form()
- What is a cookie and what kinds of things are they commonly used for?
 * A cookie is 
- What is the session object in Flask?
 * A session object
- What does Flask's `jsonify()` do?
 * jsonify() turns data into JSON so that it can be used as a response

# Testing

Click to return back to the [README.md](README.md)

## Browser Compatibility and Responsiveness 

For each of my pages I will check them against the top 3 web browsers - Google chrome, Firefox and Microsoft Edge. I initialy checked that all the elements were loading as they should on all 3 browsers.
Once I confirmed they were working as expected I then went into the devtools and changed the viewport width to check the layout and styles against different device sizes.

| Browser        | Screen Size | Image |
| :----:         |    :----:   | :----:|
| Chrome         | Desktop     | ![Home Page Desktop View](bookmarked/documentation/testing/img/chrome_desktop.jpg)  | 
| Firefox        | Desktop     | ![Home Page Desktop View](bookmarked/documentation/testing/img/firefox_desktop.jpg) |
| Microsoft Edge | Desktop     | ![Home Page Desktop View](bookmarked/documentation/testing/img/edge_desktop.jpg)   |
|                |             |                                                                                     |
| Chrome         | Ipad        | ![Home Page Desktop View](bookmarked/documentation/testing/img/chrome_tablet.jpg) | 
| Firefox        | Ipad        | ![Home Page Desktop View](bookmarked/documentation/testing/img/firefox_tablet.jpg)|
| Microsoft Edge | Ipad        | ![Home Page Desktop View](bookmarked/documentation/testing/img/edge_tablet.jpg))   |
|                |             |                                                                                     | 
| Chrome         | Mobile      | ![Home Page Mobile View](bookmarked/documentation/testing/img/chrome_mobile.jpg)   | 
| Firefox        | Mobile      | ![Home Page Mobile View](bookmarked/documentation/testing/img/firefox_mobile.jpg)  |
| Microsoft Edge | Mobile      | ![Home Page Mobile View](bookmarked/documentation/testing/img/edge_mobile.jpg)     |

## Code Validation

### HTML Validation

Once I had finished my website I ran each page throigh a HTML validator to ensure that the code was correct.

| Page                                  | Validation Result                                     |
| :----:                                |    :----:                                                                              | 
| Login Page Validator                  | ![Login Page HTML Validation](bookmarked/documentation/testing/img/login_page_validator.jpg) |
| Signup Page Validator                 | ![Login Page HTML Validation](bookmarked/documentation/testing/img/signup_page_validator.jpg) |
| Profile Page Validator                | ![Login Page HTML Validation](bookmarked/documentation/testing/img/home_page_validator.jpg) |
| Bookshelf Page Validator              | ![Login Page HTML Validation](bookmarked/documentation/testing/img/bookshelf_page_validator.jpg) |
| Add Bookshelf Page Validator          | ![Login Page HTML Validation](bookmarked/documentation/testing/img/add_bookshelf_page_validator.jpg) |
| Book Page Validator                   | ![Login Page HTML Validation](bookmarked/documentation/testing/img/book_page_validator.jpg) |
| Add Book Page Validator               | ![Login Page HTML Validation](bookmarked/documentation/testing/img/add_book_page_validator.jpg) |
| Book Generator Page Validator         | ![Login Page HTML Validation](bookmarked/documentation/testing/img/book_generate_page_validator.jpg) |
| Book Generator Results Page Validator | ![Login Page HTML Validation](bookmarked/documentation/testing/img/book_generator_result_page_validator.jpg) |



### CSS Validation

I ran my CSS through a validator to ensure that it was correct. It passed the validation and came back with no errors.
![CSS Validator](bookmarked/documentation/testing/img/css_validator.jpg)

### PEP8 Validation 

I also ran my Python code through a PEP8 Validator to make sure that it was PEP8 compliant 
![PEP8 Validator](bookmarked/documentation/testing/img/python_validation.jpg)


### User Story Testing

Once I had finished the app I decided to go through and test each element to make sure they were working correctly.

| User Story:                                               | As a user I want to be able to create an account                              |        | 
| :----:                                                    | :----:                                                                        | :----: |
|Expected Outcome                                           | ScreenShot                                                                    | Result |
|Show any errors if user leaves out inputs in form          |![login error](bookmarked/documentation/testing/img/login_error.jpg)           | Pass   |
|If user has filled out form correctly inputs will be green |![login correct](bookmarked/documentation/testing/img/login_correct.jpg)       | Pass   |
|Redirect user to profile after creating account            |![accountcreated](bookmarked/documentation/testing/img/account_created.jpg)    | Pass   |

| User Story:                                               | As a user i want to be able to log into my account                            |        | 
| :----:                                                    | :----:                                                                        | :----: |
|Expected Outcome                                           | ScreenShot                                                                    | Result |
|Display message if user enters wrong passwor/username      |![incorrect login](bookmarked/documentation/testing/img/incorrect_login.jpg)   | Pass   |
|Display welcome message if user logs in correctly          |![correct login](bookmarked/documentation/testing/img/correct_login.jpg)       | Pass   |

| User Story:                                                | As a user i want to be able to log into my account                                     |        | 
| :----:                                                     | :----:                                                                                 | :----: |
|Expected Outcome                                            | ScreenShot                                                                             | Result |
|Show an error if user leaves out inputs in form             |![add book error](bookmarked/documentation/testing/img/add_book_error.jpg)              | Pass   |
|Display message when book is created to notify user         |![add book successful](bookmarked/documentation/testing/img/add_book_successful.jpg)    | Pass   |

| User Story:                                                | As a user I want to be able to easily delete books                                  |        | 
| :----:                                                     | :----:                                                                              | :----: |
|Expected Outcome                                            | ScreenShot                                                                          | Result |
|Book is removed from books displayed books                  |![delete book before](bookmarked/documentation/testing/img/delete_book_before.jpg)   | Pass   |
|                                                            |![delete book after](bookmarked/documentation/testing/img/delete_book_after.jpg)     | Pass   |
|Display message notifying user book gas been removed         |![delete book before](bookmarked/documentation/testing/img/book_deleted.jpg)         | Pass   |

| User Story:                                                | As a user I want to be able to easily edit books                                    |        | 
| :----:                                                     | :----:                                                                              | :----: |
|Expected Outcome                                            | ScreenShot                                                                          | Result |
|Display message notifying user book as been edited          |![successful edit](bookmarked/documentation/testing/img/successful_edit.jpg)         | Pass   |
|Update book with user edits                                 |![show edit](bookmarked/documentation/testing/img/show_edit.jpg)                     | Pass   |

| User Story:                                                | As a user I want to be able to easily create bookshelves                            |        | 
| :----:                                                     | :----:                                                                              | :----: |
|Expected Outcome                                            | ScreenShot                                                                          | Result |
|Show an error if user leaves out inputs in form             |![bookcase created](bookmarked/documentation/testing/img/bookcase_created.jpg)       | Pass   |
|Display new bookcase                                        |![bookcase created](bookmarked/documentation/testing/img/bookcase_created.jpg)       | Pass   |

| User Story:                                                | As a user I want to be able to easily delete bookshelves                              |        | 
| :----:                                                     | :----:                                                                                | :----: |
|Expected Outcome                                            | ScreenShot                                                                            | Result |
|Book is removed from bookshelf  displayed bookshelves       |![bookcase created](bookmarked/documentation/testing/img/bookshelf_delete_message.jpg) | Pass   |
|Display message notifying user bookshelf has been removed   |![bookcase created](bookmarked/documentation/testing/img/bookshelf_delete_after.jpg)   | Pass   |

| User Story:                                                | As a user I want to be able to add comments to my books                               |        | 
| :----:                                                     | :----:                                                                                | :----: |
|Expected Outcome                                            | ScreenShot                                                                            | Result |
|Display message notifying user comment has been added       |![bookcase created](bookmarked/documentation/testing/img/comment_added.jpg)            | Pass   |
|Display users comment                                       |![bookcase created](bookmarked/documentation/testing/img/comment_displayed.jpg)        | Pass   |

| User Story:                                                | As a user I want to be able to delete comments from my books                          |        | 
| :----:                                                     | :----:                                                                                | :----: |
|Expected Outcome                                            | ScreenShot                                                                            | Result |
|Display message notifying user comment has been deleted     |![bookcase created](bookmarked/documentation/testing/img/comment_delete.jpg)           | Pass   |
|Remove comment from page                                    |![bookcase created](bookmarked/documentation/testing/img/comment_delete_display.jpg)   | Pass   |

| User Story:                                                | As a user i want to be able to randomly generate a book from my collections           |        | 
| :----:                                                     | :----:                                                                                | :----: |
|Expected Outcome                                            | ScreenShot                                                                            | Result |
|Display forms with book generations options                 |![bookcase created](bookmarked/documentation/testing/img/generate_book.jpg)            | Pass   |
|If no books are found display message to user               |![bookcase created](bookmarked/documentation/testing/img/generate_error.jpg)           | Pass   |
|Display generated book                                      |![bookcase created](bookmarked/documentation/testing/img/generate_result.jpg)          | Pass   |

| User Story:                                                | As a user i want to be able to search through my books                                |        | 
| :----:                                                     | :----:                                                                                | :----: |
|Expected Outcome                                            | ScreenShot                                                                            | Result |
|Display message if no books were found                      |![bookcase created](bookmarked/documentation/testing/img/search_error.jpg)             | Pass   |
|Display search results                                      |![bookcase created](bookmarked/documentation/testing/img/search_results.jpg)           | Pass   |

### Manual Testing

| Test                   | Expected Outcome                                                                         | Result   | 
| :----:                 |  :----:                                                                                  | :----:   |
| Brand redired          | Redirects user to profile page when they click on teh brand name in navbar               | Pass     |
| Nav Hover              | Navbar link background change when user hovers over link                                 | Pass     |
| Nav Link - Profile     | Navbar profile link directs user to profile page                                         | Pass     |
| Nav Link - bookshelves | Navbar bookshelf link directs user to bookshelves page                                   | Pass     |
| Nav Link - Log Out     | Navbar log out link logs user out of their account                                       | Pass     |
| Buttons hover effect   | All buttons throughout the page display a hover effect when user hovers over them        | Pass     |
| Buttons focus effect   | All buttons throughout the page display a focus effect when user focuses on them         | Pass     |


## Unfixed Bugs
There are no remaining bugs that I am aware of.
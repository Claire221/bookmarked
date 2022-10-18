
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
![HTML Validator](bookmarked/documentation/testing/img/htmls_validator.jpg)

### CSS Validation

I ran my CSS through a validator to ensure that it was correct. It passed the validation and came back with no errors.
![CSS Validator](bookmarked/documentation/testing/img/css_validator.jpg)

### PEP8 Validation 

I also ran my Python code through a PEP8 Validator to make sure that it was PEP8 compliant 
![PEP8 Validator](bookmarked/documentation/testing/img/python_validation.jpg)

## User Story Testing

Once I had finished the app I decided to go through and test each element to make sure they were working correctly.

### Account Creation

First I checked that users could create accounts successfully
![Account Creation](bookmarked/documentation/testing/img/signup_before.jpg)
![Account Creation](bookmarked/documentation/testing/img/signup_after.jpg)

### Create Bookshelf

I then checked the create bookshelf function
![Bookshelf Creation](bookmarked/documentation/testing/img/add_bookshelf_before.jpg)
![Bookshelf Creation](bookmarked/documentation/testing/img/add_bookshelf2.jpg)
![Bookshelf Creation](bookmarked/documentation/testing/img/add_bookshelf.jpg)

### Delete Bookshelf

I then wanted to test that the delete bookshelf feature deleted the bookshelf successfully.
![Delete Bookshelf](bookmarked/documentation/testing/img/bookshelf_delete_before.jpg)
![Delete Bookshelf](bookmarked/documentation/testing/img/bookshelf_delete_after.jpg)

### Delete Bookshelf - Not user who created it

### Create Book

I wanted to test that users could successfuly add books so I created a few test books.

![Add Book](bookmarked/documentation/testing/img/add_book_before.jpg)
![Add Book](bookmarked/documentation/testing/img/add_book_before2.jpg)
![Add Book](bookmarked/documentation/testing/img/add_book_after.jpg)

### Delete Book

I wanted to test that users could successfuly delete a book so I created a test book that I could test the function on.
![Delete Book](bookmarked/documentation/testing/img/delete_book_before.jpg)
![Delete Book](bookmarked/documentation/testing/img/delete_book_after.jpg)

### Edit Book

The users have the option to edit books to update the title, description, colour ect so I wandted to check that this works.
![Edit Book](bookmarked/documentation/testing/img/edit_book_before.jpg)
![Edit Book](bookmarked/documentation/testing/img/edit_book_after.jpg)

### Generate Book From Bookshelves 

There is also a feature where users can generate a random book based on different conditions so I wanted to test that these were all working correctly. I started by testing the bookshelf generation function

![Bookshelf Generator ](bookmarked/documentation/testing/img/bookshelf_generator_before.jpg)
![Bookshelf Generator ](bookmarked/documentation/testing/img/bookshelf_generator_after.jpg)

### Generate Book From Authors

I then tested the generate from authors function.
![Author Generator ](bookmarked/documentation/testing/img/author_generator_before.jpg)
![Author Generator ](bookmarked/documentation/testing/img/author_generator_after.jpg)

### Generate Book From Tags

### Generate Book From All Books

Finally I tested the generate from all the users books function.
![Library Generator](bookmarked/documentation/testing/img/random_generator_before.jpg)
![Library Generator](bookmarked/documentation/testing/img/random_generator_after.jpg)

## Unfixed Bugs
    list out any unfinished bugs you might have, where applicable... if none, don't just put "I have no bugs"... put something like: "There are no remaining bugs that I am aware of."
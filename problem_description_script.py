import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def generate_problem_comment_with_selenium(url: str, directory_path: str = "."):
    try:
        # Configure Selenium WebDriver
        driver = webdriver.Chrome()
        driver.get(url)
        
        # Extract problem details using Selenium
        problem_title = driver.find_element(By.XPATH, "//div[contains(@class, 'text-title-large')]/a").text.strip()
        problem_number = problem_title.split(".")[0]
        problem_title_for_file_name = url.split("/")[4]
        difficulty_text = driver.find_element(By.XPATH, "//div[contains(@class, 'text-difficulty')]").text.strip()
        description_content = driver.find_element(By.XPATH, "//div[@data-track-load='description_content']").text.strip()

        # Format the problem details into a comment
        comment = f"""\"\"\"
Problem Number: {problem_title}
Difficulty Level: {difficulty_text}
{url}

********************************************************************************

{description_content}
\"\"\"
"""
        # Ensure the directory exists
        os.makedirs(directory_path, exist_ok=True)
        
        # Write the comment to the file in the specified directory
        file_path = os.path.join(directory_path, f"{problem_number}.{problem_title_for_file_name}.py")
        with open(file_path, "w") as my_file:
            my_file.write(comment)

    except Exception as e:
        return f"Error: Unable to fetch problem details. {str(e)}"

    finally:
        driver.quit()

if __name__ == "__main__":
    url = input("Enter a link to LeetCode problem : ")
    directory_path = input("Enter a directory name to create a file : ")
    generate_problem_comment_with_selenium(url, directory_path if directory_path else ".")
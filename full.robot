*** Settings ***
Library    SeleniumLibrary
Library    DateTime

*** Variables ***
${browser}    chrome
${url}        https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=2463491726286621147&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062011&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1
${screenshot_dir}    C:/Users/Plabani/Documents/MY/

*** Test Cases ***
Capture Full Page Screenshot
    Open Browser    ${url}    ${browser}     options= add_experimental_option("detach",True)
    Maximize Browser Window
    Sleep    5s  # Allow time for the page to fully load

# Generate timestamp for filename
    ${timestamp}=    Get Current Date    result_format=%Y-%m-%d_%H-%M-%S

    # Get page dimensions
    ${scroll_height}=    Execute JavaScript    return document.body.scrollHeight
    ${viewport_width}    ${viewport_height}=    Get Window Size

    # Define number of screenshots needed
    ${total_scrolls}=    Evaluate    ${scroll_height} / ${viewport_height}

    # Initialize part number
    ${part_number}=    Set Variable    1

    FOR    ${i}    IN RANGE    ${total_scrolls}
        # Scroll down by viewport height
        Execute JavaScript    window.scrollTo(0, ${viewport_height} * ${i});
        Sleep    2s  # Allow time for the page to render

        # Capture screenshot
        ${current_filename}=    Set Variable    ${screenshot_dir}fullpage_screenshot_${timestamp}_part_${part_number}.png
        Capture Page Screenshot    ${current_filename}

        # Increment part number
        ${part_number}=    Evaluate    ${part_number} + 1
    END

    # Close the browser
    Close Browser
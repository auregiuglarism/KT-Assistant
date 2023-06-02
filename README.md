# KT-Assistant

### Website
A website has been implemented in order to play around with the model in an intuitive way, offering a straightforward interface for uploading text and asking questions that the model will evaluate. To get started using the website, follow the steps outlined below:

1. **Install Dependencies**: Ensure you have Python installed on your machine. Then, navigate to the root directory where the `requirements.txt` file is saved and install the necessary Python packages by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

   This will install all the necessary libraries and dependencies needed for the server side of the web application.

2. **Run the Server**: Next, you need to start the server that will interact with the model. This can be done by running the Python script set up for this purpose. In the terminal, navigate to the directory containing the server script and run:

    ```
    python server.py
    ```

   If everything is set up correctly, you should see output indicating that the server is running, usually with a line like `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`.

3. **Open the Website**: Now, with the server running, you can interact with the model via the website. Open the HTML file `index.html` in any web browser by double clicking the HTML file or dragging it into an open browser window.

4. **Usage**: On the website, you'll first see a textbox where you can paste a document's text or upload a text file. Once the document is uploaded or pasted, you can insert your claim in the textbox below and click 'Submit'. The model will then evaluate the claim based on the provided document, and the prediction result will be displayed on the webpage.

Remember, the server must be kept running while you are using the website. If you close the server, the website will not be able to interact with the model.
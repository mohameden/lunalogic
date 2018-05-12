<!DOCTYPE html>
<html lang="en">

<head>
    <title>Price publisher</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="http://mindmup.github.io/editable-table/mindmup-editabletable.js"></script>
<body>
    <div class="container">
        <div class="jumbotron">
            <h1 >Price publisher</h2>
            <p>Publish the currency value using USD as reference.</p>
        </div>
        <div class="row">
            <div class="col-sm-5">
                <form id="form" action="/publish" method="post">
                    <div class="form-group">
                        <label for="country">Country:</label>
                        <input type="text" class="form-control" id="country" name="country"></input>
                    </div>
                    <div class="form-group">
                        <label for="price">Price:</label>
                        <input type="text" class="form-control" id="price" name="price"></input>
                    </div>
                    <div class="form-group">
                        <label for="description">Description:</label>
                        <textarea rows="5" class="form-control" id="description" name="description"></textarea>
                    </div>
                    <button type="submit" class="btn btn-success" id="publish">Publish</button>
                </form>
            </div>
            <div class="col-sm-7"></div>
        </div>

    </div>

</body>
</html>

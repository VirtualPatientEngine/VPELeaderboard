<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Algorithm Metrics</title>

  <!-- Intro.js -->
  <script src="https://cdn.jsdelivr.net/npm/intro.js@7.2.0/intro.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/intro.js@7.2.0/minified/introjs.min.css">

  <!-- DataTables CSS -->
  <link rel="stylesheet" href="https://cdn.datatables.net/2.0.1/css/dataTables.dataTables.css">
  <link rel="stylesheet" href="https://cdn.datatables.net/buttons/3.0.1/css/buttons.dataTables.css">

  <!-- Google Fonts for Icons -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

  <!-- jQuery -->
  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>

  <!-- DataTables JavaScript -->
  <script src="https://cdn.datatables.net/2.0.1/js/dataTables.js"></script>
  <script src="https://cdn.datatables.net/buttons/3.0.1/js/dataTables.buttons.js"></script>
  <script src="https://cdn.datatables.net/buttons/3.0.1/js/buttons.dataTables.js"></script>

  <!-- Export Libraries -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.7/pdfmake.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.7/vfs_fonts.js"></script>
  <script src="https://cdn.datatables.net/buttons/3.0.1/js/buttons.html5.min.js"></script>
  <script src="https://cdn.datatables.net/buttons/3.0.1/js/buttons.print.min.js"></script>

  <style>
    .container {
      padding: 20px;
    }

    /* Ensure table is centered and does not stretch unnecessarily */
    .dataTables_wrapper {
      max-width: 100%;
      margin: auto;
      overflow-x: hidden;
    }

    /* Ensure export buttons are fully left-aligned and search bar fully right-aligned */
    .export-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      max-width: 85%;
      margin: auto;
    }

    /* Fix Export Buttons Alignment */
    .dt-buttons {
      display: flex;
      gap: 3px; /* Minimized gap between buttons */
    }

    /* Fix Search Bar Alignment */
    .dataTables_filter {
      margin-left: auto; /* Push search bar to the right */
      text-align: right;
    }

    .dataTables_filter {
      text-align: right;
    }
    .dataTables_filter label {
      font-weight: bold;
    }

    .dataTables_filter input {
      padding: 6px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }

    #table1 {
      width: 100%;
      table-layout: fixed;  /* Forces equal width for all columns */
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Add shadow to table */
    }

    /* Style table headers */
    #table1 th ,#table1 td {
      padding: 12px 15px;
      text-align: center;
      vertical-align: middle;
      word-wrap: break-word;
      white-space: normal;
      font-size: small;
      width: 25%;
      border: 1px solid #ddd; /* Add light borders between columns */
    }

    #table1 thead th {
      background-color: #f1f1f1; /* Light gray background */
      font-weight: bold;
      border-bottom: 2px solid #ddd; /* Add a thin line under the header */
    }

    #table1 {
      width: 100%;
      table-layout: fixed; 
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Add shadow to table */
    }

    /* Row Styling */
    tr {
      border-bottom: 1px solid #ddd; /* Light border between rows */
    }

    .child-row-content {
      text-align: justify;
      text-justify: inter-word;
      word-wrap: break-word;
      white-space: normal;
      max-width: 100%;
      padding: 10px;
      font-size: small;
    }
  </style>
</head>
<body class="container">
  <p><i class="footer">This page was last updated on 2025-04-26 21:06:41 UTC</i></p>
  
  <!-- Export Buttons and Search Bar at the Top -->
  <div class="export-container">
    <div class="dt-buttons"></div> <!-- Export buttons on the left -->
    <div class="dataTables_filter"></div> <!-- Search bar on the right -->
  </div>
         
  <!-- Algorithm Metrics Table -->
  <div data-intro="This table displays algorithm performance metrics.">
    <h3 id="algorithm_metrics">Algorithm Metrics Table</h3>
    <table id="table1" class="display wrap" style="width:100%">
    <thead>
        <tr>
            <!-- <th>Abstract</th> -->
            
                <th>Algorithm</th>
            
                <th>Metric 1</th>
            
                <th>Metric 2</th>
            
                <th>Metric 3</th>
            
        </tr>
    </thead>

    <tbody>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 1</td>
            
                <td>0.86</td>
            
                <td>0.35</td>
            
                <td>0.8</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 2</td>
            
                <td>0.94</td>
            
                <td>0.32</td>
            
                <td>0.9</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 3</td>
            
                <td>0.91</td>
            
                <td>0.34</td>
            
                <td>0.83</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 4</td>
            
                <td>0.89</td>
            
                <td>0.33</td>
            
                <td>0.87</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 5</td>
            
                <td>0.82</td>
            
                <td>0.29</td>
            
                <td>0.97</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 6</td>
            
                <td>0.82</td>
            
                <td>0.34</td>
            
                <td>0.81</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 7</td>
            
                <td>0.81</td>
            
                <td>0.21</td>
            
                <td>0.85</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 8</td>
            
                <td>0.93</td>
            
                <td>0.23</td>
            
                <td>0.93</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 9</td>
            
                <td>0.89</td>
            
                <td>0.21</td>
            
                <td>0.8</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 10</td>
            
                <td>0.91</td>
            
                <td>0.25</td>
            
                <td>0.77</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 11</td>
            
                <td>0.8</td>
            
                <td>0.26</td>
            
                <td>0.82</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 12</td>
            
                <td>0.95</td>
            
                <td>0.24</td>
            
                <td>0.79</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 13</td>
            
                <td>0.92</td>
            
                <td>0.32</td>
            
                <td>0.97</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 14</td>
            
                <td>0.83</td>
            
                <td>0.25</td>
            
                <td>0.94</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 15</td>
            
                <td>0.83</td>
            
                <td>0.24</td>
            
                <td>0.9</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 16</td>
            
                <td>0.83</td>
            
                <td>0.28</td>
            
                <td>0.96</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 17</td>
            
                <td>0.85</td>
            
                <td>0.22</td>
            
                <td>0.94</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 18</td>
            
                <td>0.88</td>
            
                <td>0.32</td>
            
                <td>0.79</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 19</td>
            
                <td>0.86</td>
            
                <td>0.21</td>
            
                <td>0.96</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 20</td>
            
                <td>0.84</td>
            
                <td>0.35</td>
            
                <td>0.88</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 21</td>
            
                <td>0.89</td>
            
                <td>0.32</td>
            
                <td>0.94</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 22</td>
            
                <td>0.82</td>
            
                <td>0.23</td>
            
                <td>0.97</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 23</td>
            
                <td>0.84</td>
            
                <td>0.2</td>
            
                <td>0.83</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 24</td>
            
                <td>0.85</td>
            
                <td>0.32</td>
            
                <td>0.78</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 25</td>
            
                <td>0.87</td>
            
                <td>0.31</td>
            
                <td>0.8</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 26</td>
            
                <td>0.92</td>
            
                <td>0.31</td>
            
                <td>0.85</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 27</td>
            
                <td>0.83</td>
            
                <td>0.32</td>
            
                <td>0.95</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 28</td>
            
                <td>0.88</td>
            
                <td>0.21</td>
            
                <td>0.96</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 29</td>
            
                <td>0.89</td>
            
                <td>0.25</td>
            
                <td>0.75</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 30</td>
            
                <td>0.81</td>
            
                <td>0.22</td>
            
                <td>0.87</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 31</td>
            
                <td>0.89</td>
            
                <td>0.33</td>
            
                <td>0.85</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 32</td>
            
                <td>0.83</td>
            
                <td>0.29</td>
            
                <td>0.8</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 33</td>
            
                <td>0.81</td>
            
                <td>0.25</td>
            
                <td>0.78</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 34</td>
            
                <td>0.94</td>
            
                <td>0.21</td>
            
                <td>0.83</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 35</td>
            
                <td>0.94</td>
            
                <td>0.25</td>
            
                <td>0.98</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 36</td>
            
                <td>0.92</td>
            
                <td>0.25</td>
            
                <td>0.83</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 37</td>
            
                <td>0.85</td>
            
                <td>0.31</td>
            
                <td>0.87</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 38</td>
            
                <td>0.81</td>
            
                <td>0.3</td>
            
                <td>0.92</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 39</td>
            
                <td>0.9</td>
            
                <td>0.33</td>
            
                <td>0.84</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 40</td>
            
                <td>0.87</td>
            
                <td>0.27</td>
            
                <td>0.98</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 41</td>
            
                <td>0.82</td>
            
                <td>0.22</td>
            
                <td>0.98</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 42</td>
            
                <td>0.87</td>
            
                <td>0.31</td>
            
                <td>0.81</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 43</td>
            
                <td>0.81</td>
            
                <td>0.31</td>
            
                <td>0.87</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 44</td>
            
                <td>0.94</td>
            
                <td>0.28</td>
            
                <td>0.82</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 45</td>
            
                <td>0.84</td>
            
                <td>0.32</td>
            
                <td>0.82</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 46</td>
            
                <td>0.9</td>
            
                <td>0.27</td>
            
                <td>0.76</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 47</td>
            
                <td>0.85</td>
            
                <td>0.28</td>
            
                <td>0.9</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 48</td>
            
                <td>0.88</td>
            
                <td>0.26</td>
            
                <td>0.87</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 49</td>
            
                <td>0.88</td>
            
                <td>0.2</td>
            
                <td>0.76</td>
            
        </tr>
        
        <tr>
            <!-- <td class="abstract-toggle">
                <i class="material-icons toggle-icon">visibility_off</i>
                <div class="abstract-content">None</div>
            </td> -->
            
                <td>Algo 50</td>
            
                <td>0.83</td>
            
                <td>0.22</td>
            
                <td>0.82</td>
            
        </tr>
        
    </tbody>
    </table>
  </div>

  <script>
  $(document).ready(function() {
      var table = $('#table1').DataTable({
          paging: true,
          autoWidth: false,
          scrollX: false,
          fixedHeader: true,
          // dom: '<"export-container"Bf>rtip', // Ensures search bar is on the right
          // buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
          columnDefs: [
              { "className": "dt-center", "targets": "_all" },
              { "width": "120px", "targets": 0 },
              { "width": "160px", "targets": 1 },
              { "width": "80px", "targets": [2, 3] }
          ]
      });

      $(".dataTables_filter").addClass("text-right");
    });

    document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".abstract-toggle .toggle-icon").forEach(icon => {
      icon.addEventListener("click", function () {
        const abstract = this.nextElementSibling;
        if (abstract.style.display === "none" || abstract.style.display === "") {
          abstract.style.display = "block";
          this.textContent = "visibility";  // Change icon
        } else {
          abstract.style.display = "none";
          this.textContent = "visibility_off";  // Revert icon
          }

    })
        });
  });
  </script>
</body>
</html>
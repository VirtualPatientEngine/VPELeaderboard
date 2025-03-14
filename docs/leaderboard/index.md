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

    /* Ensure table is centered */
    .dataTables_wrapper {
      max-width: 85%;
      margin: auto;
      overflow-x: hidden;
    }

    /* Export buttons and search bar */
    .export-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: nowrap;
      margin-bottom: 10px;
      max-width: 85%;
      margin: auto;
    }

    /* Table column spacing */
    #table1 th, #table1 td {
      padding: 10px 12px;
      text-align: center;
      vertical-align: middle;
      white-space: nowrap;
    }

    /* Table header style */
    #table1 thead th {
      background-color: #e0e0e0;
      font-weight: bold;
      border-bottom: 2px solid #bdbdbd;
    }

    /* Abstract styling */
    .abstract-toggle {
      cursor: pointer;
      text-align: center;
    }

    .abstract-content {
      display: none;
      background: #f9f9f9;
      padding: 10px;
      border-radius: 5px;
      max-width: 500px;
      word-wrap: break-word;
    }
  </style>
</head>
<body class="container">
  <p><i class="footer">This page was last updated on 2025-03-13 21:41:29 UTC</i></p>

  <!-- Intro Button -->
  <div class="note info" onclick="startIntro()">
    <p>
      <button type="button" class="intro-button">
        Click here for a quick intro of the page! <i class="material-icons">help</i>
      </button>
    </p>
  </div>
  
  <!-- Export Buttons and Search Bar at the Top -->
  <div class="export-container">
    <div class="dt-buttons"></div> <!-- Export buttons -->
    <div class="dataTables_filter"></div> <!-- Search bar -->
  </div>
         
  <!-- Algorithm Metrics Table -->
  <div data-intro="This table displays algorithm performance metrics.">
    <h3 id="algorithm_metrics">Algorithm Metrics Table</h3>
    <table id="table1" class="display wrap" style="width:100%">
        <thead>
            <tr>
                <th>Abstract</th>
                
                    <th>Rank</th>
                
                    <th>Algorithm Name</th>
                
                    <th>Task/Data</th>
                
                    <th>Metric 1</th>
                
                    <th>Metric 2</th>
                
                    <th>Metric 3</th>
                
            </tr>
        </thead>
        
        <tbody>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 1</td>
                
                    <td>Algo 1</td>
                
                    <td>Task A</td>
                
                    <td>0.85</td>
                
                    <td>0.75</td>
                
                    <td>0.65</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 2</td>
                
                    <td>Algo 2</td>
                
                    <td>Task B</td>
                
                    <td>0.87</td>
                
                    <td>0.77</td>
                
                    <td>0.67</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 3</td>
                
                    <td>Algo 3</td>
                
                    <td>Task C</td>
                
                    <td>0.89</td>
                
                    <td>0.79</td>
                
                    <td>0.69</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 4</td>
                
                    <td>Algo 4</td>
                
                    <td>Task D</td>
                
                    <td>0.91</td>
                
                    <td>0.81</td>
                
                    <td>0.71</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 5</td>
                
                    <td>Algo 5</td>
                
                    <td>Task E</td>
                
                    <td>0.93</td>
                
                    <td>0.83</td>
                
                    <td>0.73</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 6</td>
                
                    <td>Algo 6</td>
                
                    <td>Task A</td>
                
                    <td>0.85</td>
                
                    <td>0.75</td>
                
                    <td>0.65</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 7</td>
                
                    <td>Algo 7</td>
                
                    <td>Task B</td>
                
                    <td>0.87</td>
                
                    <td>0.77</td>
                
                    <td>0.67</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 8</td>
                
                    <td>Algo 8</td>
                
                    <td>Task C</td>
                
                    <td>0.89</td>
                
                    <td>0.79</td>
                
                    <td>0.69</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 9</td>
                
                    <td>Algo 9</td>
                
                    <td>Task D</td>
                
                    <td>0.91</td>
                
                    <td>0.81</td>
                
                    <td>0.71</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 10</td>
                
                    <td>Algo 10</td>
                
                    <td>Task E</td>
                
                    <td>0.93</td>
                
                    <td>0.83</td>
                
                    <td>0.73</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 11</td>
                
                    <td>Algo 11</td>
                
                    <td>Task A</td>
                
                    <td>0.85</td>
                
                    <td>0.75</td>
                
                    <td>0.65</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 12</td>
                
                    <td>Algo 12</td>
                
                    <td>Task B</td>
                
                    <td>0.87</td>
                
                    <td>0.77</td>
                
                    <td>0.67</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 13</td>
                
                    <td>Algo 13</td>
                
                    <td>Task C</td>
                
                    <td>0.89</td>
                
                    <td>0.79</td>
                
                    <td>0.69</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 14</td>
                
                    <td>Algo 14</td>
                
                    <td>Task D</td>
                
                    <td>0.91</td>
                
                    <td>0.81</td>
                
                    <td>0.71</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 15</td>
                
                    <td>Algo 15</td>
                
                    <td>Task E</td>
                
                    <td>0.93</td>
                
                    <td>0.83</td>
                
                    <td>0.73</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 16</td>
                
                    <td>Algo 16</td>
                
                    <td>Task A</td>
                
                    <td>0.85</td>
                
                    <td>0.75</td>
                
                    <td>0.65</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 17</td>
                
                    <td>Algo 17</td>
                
                    <td>Task B</td>
                
                    <td>0.87</td>
                
                    <td>0.77</td>
                
                    <td>0.67</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 18</td>
                
                    <td>Algo 18</td>
                
                    <td>Task C</td>
                
                    <td>0.89</td>
                
                    <td>0.79</td>
                
                    <td>0.69</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 19</td>
                
                    <td>Algo 19</td>
                
                    <td>Task D</td>
                
                    <td>0.91</td>
                
                    <td>0.81</td>
                
                    <td>0.71</td>
                
            </tr>
            
            <tr>
                <!-- Abstract Toggle -->
                <td class="abstract-toggle">
                    <i class="material-icons toggle-icon">visibility_off</i>
                    <div class="abstract-content">No abstract available</div>
                </td>
        
                <!-- Ensure each column is rendered separately -->
                
                    <td>🏅 20</td>
                
                    <td>Algo 20</td>
                
                    <td>Task E</td>
                
                    <td>0.93</td>
                
                    <td>0.83</td>
                
                    <td>0.73</td>
                
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
          dom: '<"export-container"Bf>rtip', 
          buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
          columnDefs: [
              { "className": "dt-center", "targets": "_all" },
              { "width": "120px", "targets": 0 },
              { "width": "160px", "targets": 1 },
              { "width": "80px", "targets": [2, 3, 4] }
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
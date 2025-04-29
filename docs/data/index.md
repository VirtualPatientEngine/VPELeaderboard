<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Time-series Forecasting Articles</title>

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

    /* Ensure table does not exceed window width */
    .dataTables_wrapper {
      max-width: 100%;
      margin: auto;
      overflow-x: auto;
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
      gap: 3px;
    }

    /* Fix Search Bar Alignment */
    .dataTables_filter {
      margin-left: auto;
      text-align: right;
    }

    #table1 th, #table1 td {
      padding: 12px 15px;
      text-align: center;
      vertical-align: middle;
      word-wrap: break-word;
      white-space: normal;
      font-size: small;
      width: 25%;
      border: 1px solid #ddd; /* Add light borders between columns */
    }

    /* Header Styling */
    #table1 thead th {
      background-color: #f1f1f1; /* Light gray background */
      font-weight: bold;
      border-bottom: 2px solid #ddd; /* Add a thin line under the header */
    }

    /* Abstract toggle styling */
    .abstract-toggle {
      cursor: pointer;
      text-align: center;
      font-size: small;
    }

    /* Abstract content styling */
    .abstract-content {
      text-justify: inter-word;
      background: #f9f9f9;
      padding: 15px;
      border-radius: 8px;
      word-wrap: break-word;
      white-space: normal;
      max-width: 100%;
      font-size: 14px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Soft shadow for the abstract content */
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
  <p><i class="footer">This page was last updated on 2025-04-29 12:09:24 UTC</i></p>

  <div class="export-container">
    <div class="dt-buttons"></div>
    <div class="dataTables_filter"></div>
  </div>

  <div>
    <h3 id="algorithm_metrics">System Biology Models</h3>
    <table id="table1" class="display wrap" style="width:100%">
      <thead>
        <tr>
          <th>Abstract</th>
          <th>Model Name</th>
          <th>Number of Species</th>
          <th>Number of Parameters</th>
        </tr>
      </thead>

      <tbody>
        
        <tr>
          <td class="abstract-toggle">
            <i class="material-icons toggle-icon">visibility_off</i>
          </td>
          <td>Teusink2000_Glycolysis</td>
          <td>26</td>
          <td>15</td>
        </tr>
        <tr class="abstract-row" style="display:none;">
          <td colspan="4">
            <div class="abstract-content">
              <!-- Render HTML content from Python backend here -->
              <body xmlns="http://www.w3.org/1999/xhtml">
    <p>
      <b>Can yeast glycolysis be understood in terms of in vitro kinetics of the constituent enzymes? Testing biochemistry.</b>
      <br/>
      <i>Teusink,B et al.: Eur J Biochem 2000 Sep;267(17):5313-29.</i>
      <br/>
          The model reproduces the steady-state fluxes and metabolite concentrations of the branched model as given in Table 4 of the paper. It is derived from the model on JWS online, but has the ATP consumption in the succinate branch with the same stoichiometrie as in the publication. The model was successfully tested on copasi v.4.4(build 26).      <br/>
          For Vmax values, please note that there is a conversion factor of approx. 270 to convert from U/mg-protein as shown in Table 1 of the paper to mmol/(min*L_cytosol). The equilibrium constant for the ADH reaction in the paper is given for the reverse reaction (Keq = 1.45*10      <sup>4</sup>
          ). The value used in this model is for the forward reaction: 1/Keq = 6.9*10      <sup>-5</sup>
          .      <br/>
          Vmax parameters values used (in [mM/min] except VmGLT):      <table border="0" cellpadding="2" cellspacing="0">
        <tr>
          <td>
            <b>VmGLT</b>
          </td>
          <td>97.264</td>
          <td>mmol/min</td>
        </tr>
        <tr>
          <td>
            <b>VmGLK</b>
          </td>
          <td>226.45</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmPGI</b>
          </td>
          <td>339.667</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmPFK</b>
          </td>
          <td>182.903</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmALD</b>
          </td>
          <td>322.258</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmGAPDH_f</b>
          </td>
          <td>1184.52</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmGAPDH_r</b>
          </td>
          <td>6549.68</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmPGK</b>
          </td>
          <td>1306.45</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmPGM</b>
          </td>
          <td>2525.81</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmENO</b>
          </td>
          <td>365.806</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmPYK</b>
          </td>
          <td>1088.71</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmPDC</b>
          </td>
          <td>174.194</td>
          <td/>
        </tr>
        <tr>
          <td>
            <b>VmG3PDH</b>
          </td>
          <td>70.15</td>
          <td/>
        </tr>
      </table>
          The result of the G6P steady state concentration (marked in red) differs slightly from the one given in table 4. of the publication      <br/>
          Results for steady state:      <table border="0" cellpadding="2" cellspacing="0">
        <thead>
          <tr>
            <th align="left" bgcolor="#eeeeee" valign="middle"/>
            <th align="left" bgcolor="#eeeeee" valign="middle">orig. article</th>
            <th align="center" bgcolor="#eeeeee" valign="middle">this model</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <b>Fluxes[mM/min]</b>
                                 </td>
              <td/>
              <td/>
            </tr>
            <tr>
              <td>Glucose </td>
              <td>88 </td>
              <td>88 </td>
            </tr>
            <tr>
              <td>Ethanol </td>
              <td>129 </td>
              <td>129 </td>
            </tr>
            <tr>
              <td>Glycogen </td>
              <td>6 </td>
              <td>6 </td>
            </tr>
            <tr>
              <td>Trehalose </td>
              <td>4.8 </td>
              <td>4.8 </td>
              <td>(G6P flux through trehalose branch)</td>
            </tr>
            <tr>
              <td>Glycerol </td>
              <td>18.2 </td>
              <td>18.2 </td>
            </tr>
            <tr>
              <td>Succinate </td>
              <td>3.6 </td>
              <td>3.6 </td>
            </tr>
            <tr>
              <td>
                <b>Conc.[mM]</b>
                                 </td>
                <td/>
                <td/>
              </tr>
              <tr>
                <td>G6P </td>
                <td>1.07 </td>
                <td style="color: red">1.03 </td>
              </tr>
              <tr>
                <td>F6P </td>
                <td>0.11 </td>
                <td>0.11 </td>
              </tr>
              <tr>
                <td>F1,6P </td>
                <td>0.6 </td>
                <td>0.6 </td>
              </tr>
              <tr>
                <td>DHAP </td>
                <td>0.74 </td>
                <td>0.74 </td>
              </tr>
              <tr>
                <td>3PGA </td>
                <td>0.36 </td>
                <td>0.36 </td>
              </tr>
              <tr>
                <td>2PGA </td>
                <td>0.04 </td>
                <td>0.04 </td>
              </tr>
              <tr>
                <td>PEP </td>
                <td>0.07 </td>
                <td>0.07 </td>
              </tr>
              <tr>
                <td>PYR </td>
                <td>8.52 </td>
                <td>8.52 </td>
              </tr>
              <tr>
                <td>AcAld </td>
                <td>0.17 </td>
                <td>0.17 </td>
              </tr>
              <tr>
                <td>ATP </td>
                <td>2.51 </td>
                <td>2.51 </td>
              </tr>
              <tr>
                <td>ADP </td>
                <td>1.29 </td>
                <td>1.29 </td>
              </tr>
              <tr>
                <td>AMP </td>
                <td>0.3 </td>
                <td>0.3 </td>
              </tr>
              <tr>
                <td>NAD </td>
                <td>1.55 </td>
                <td>1.55 </td>
              </tr>
              <tr>
                <td>NADH </td>
                <td>0.04 </td>
                <td>0.04 </td>
              </tr>
            </tbody>
          </table>
          Authors of the publication also mentioned a few misprints in the original article:      <br/>
          in the kinetic law for      <em>ADH</em>
          :      <ol>
            <li>the species          <em>a</em>
              should denote          <em>NAD</em>
              and          <em>b</em>
            <em>Ethanol</em></li>
            <li>the last term in the equation should read          <em>bpq</em>
              /(          <em>K            <sub>ib</sub>
                K            <sub>iq</sub>
                K            <sub>p</sub></em>
              )          </li>
          </ol>
          in the kinetic law for      <em>PFK</em>
          :      <ol>
            <li>R = 1 + λ          <sub>1</sub>
              + λ          <sub>2</sub>
              + g          <sub>r</sub>
              λ          <sub>1</sub>
              λ          <sub>2</sub></li>
            <li>equation L  should read: L = L0*(..)          <sup>2</sup>
              *(..)          <sup>2</sup>
              *(..)          <sup>2</sup>
              not L = L0*(..)          <sup>2</sup>
              *(..)          <sup>2</sup>
              *(..)          </li>
          </ol>
          To make the model easier to curate, the species      <em>ATP</em>
          ,      <em>ADP</em>
          and      <em>AMP</em>
          were added. These are calculated via assignment rules from the active phosphate species,      <em>P</em>
          , and the sum of all      <em>AXP</em>
          ,      <em>SUM_P</em>
          .      </p>
          <br/>
          <p>To the extent possible under law, all copyright and related or neighbouring rights to this encoded model have been dedicated to the public domain worldwide. Please refer to      <a href="http://creativecommons.org/publicdomain/zero/1.0/" title="Creative Commons CC0">CC0 Public Domain Dedication</a>
          for more information.      </p>
          <p>In summary, you are entitled to use this encoded model in absolutely any manner you deem suitable, verbatim, or with modification, alone or embedded it in a larger context, redistribute it, commercially or not, in a restricted way or not.</p>
          <br/>
          <p>To cite BioModels Database, please use:      <a href="http://www.ncbi.nlm.nih.gov/pubmed/20587024" target="_blank">Li C, Donizelli M, Rodriguez N, Dharuri H, Endler L, Chelliah V, Li L, He E, Henry A, Stefan MI, Snoep JL, Hucka M, Le Novère N, Laibe C (2010) BioModels Database: An enhanced, curated and annotated resource for published quantitative kinetic models. BMC Syst Biol., 4:92.</a></p>
        </body>
            </div>
          </td>
        </tr>
        
        <tr>
          <td class="abstract-toggle">
            <i class="material-icons toggle-icon">visibility_off</i>
          </td>
          <td>Dwivedi2014 - Crohns IL6 Disease model - Anti-IL6R Antibody</td>
          <td>44</td>
          <td>53</td>
        </tr>
        <tr class="abstract-row" style="display:none;">
          <td colspan="4">
            <div class="abstract-content">
              <!-- Render HTML content from Python backend here -->
              <body xmlns="http://www.w3.org/1999/xhtml">
    <div class="dc:title">Dwivedi2014 - Crohns IL6 Disease model -
Anti-IL6R Antibody</div>
    <div class="dc:description">This model is comprised of four models:
<br/>
    <ul>
      <li>
        <a href="http://www.ebi.ac.uk/biomodels-main/BIOMD0000000534">[BIOMD0000000534]</a>
  Healthy Volunteer model
  <br/></li>
        <li>
          <a href="http://www.ebi.ac.uk/biomodels-main/BIOMD0000000535">[BIOMD0000000535]</a>
  Crohn&apos;s Disease - IL-6 Antibody
  <br/></li>
          <li>
            <a href="http://www.ebi.ac.uk/biomodels-main/BIOMD0000000536">[BIOMD0000000536]</a>
  Crohn&apos;s Disease - sgp130FC</li>
            <li>
              <a href="http://www.ebi.ac.uk/biomodels-main/BIOMD0000000537">[BIOMD0000000537]</a>
  Crohn&apos;s Disease - IL-6Ra Antibody
  <br/></li>
            </ul>Possible avenues for Interleukin-6 (IL-6) inhibition in
treating Crohn&apos;s disease are compared here. Each model refers to
separate ligands. The system simulates differential activity of the
ligands on the signalling of IL-6. 
<span class="st">This affects Signal Transducer and Activator of
Transcription 3</span> (STAT3) activity on the production of
biomarker C-Reactive Protein (CRP) expression.
<br/>Figures referring to this Crohn&apos;s Disease model are 3a, 4d,
4e, 4f and 5b.
<br/></div>
            <div class="dc:bibliographicCitation">
              <p>This model is described in the article:</p>
              <div class="bibo:title">
                <a href="http://identifiers.org/pubmed/24402116" title="Access to this publication">A multiscale model of
    interleukin-6-mediated immune regulation in Crohn&apos;s disease and
    its application in drug discovery and development.</a>
              </div>
              <div class="bibo:authorList">Dwivedi G, Fitz L, Hegen M, Martin
  SW, Harrold J, Heatherington A, Li C.</div>
              <div class="bibo:Journal">CPT Pharmacometrics Syst Pharmacol
  2014; 3: e89</div>
              <p>Abstract:</p>
              <div class="bibo:abstract">
                <p>In this study, we have developed a multiscale systems model
    of interleukin (IL)-6-mediated immune regulation in Crohn&apos;s
    disease, by integrating intracellular signaling with
    organ-level dynamics of pharmacological markers underlying the
    disease. This model was linked to a general pharmacokinetic
    model for therapeutic monoclonal antibodies and used to
    comparatively study various biotherapeutic strategies targeting
    IL-6-mediated signaling in Crohn&apos;s disease. Our work
    illustrates techniques to develop mechanistic models of disease
    biology to study drug-system interaction. Despite a sparse
    training data set, predictions of the model were qualitatively
    validated by clinical biomarker data from a pilot trial with
    tocilizumab. Model-based analysis suggests that strategies
    targeting IL-6, IL-6R?, or the IL-6/sIL-6R? complex are less
    effective at suppressing pharmacological markers of Crohn&apos;s
    than dual targeting the IL-6/sIL-6R? complex in addition to
    IL-6 or IL-6R?. The potential value of multiscale system
    pharmacology modeling in drug discovery and development is also
    discussed.CPT: Pharmacometrics &amp; Systems Pharmacology
    (2014) 3, e89; doi:10.1038/psp.2013.64; advance online
    publication 8 January 2014.</p>
              </div>
            </div>
            <div class="dc:publisher">
              <p>This model is hosted on 
  <a href="http://www.ebi.ac.uk/biomodels/">BioModels Database</a>
  and identified by: 
  <a href="http://identifiers.org/biomodels.db/BIOMD0000000537">BIOMD0000000537</a>.</p>
              <p>To cite BioModels Database, please use: 
  <a href="http://identifiers.org/pubmed/20587024" title="Latest BioModels Database publication">BioModels Database:
  An enhanced, curated and annotated resource for published
  quantitative kinetic models</a>.</p>
            </div>
            <div class="dc:license">
              <p>To the extent possible under law, all copyright and related or
  neighbouring rights to this encoded model have been dedicated to
  the public domain worldwide. Please refer to 
  <a href="http://creativecommons.org/publicdomain/zero/1.0/" title="Access to: CC0 1.0 Universal (CC0 1.0), Public Domain Dedication">CC0
  Public Domain Dedication</a> for more information.</p>
            </div>
          </body>
            </div>
          </td>
        </tr>
        
        <tr>
          <td class="abstract-toggle">
            <i class="material-icons toggle-icon">visibility_off</i>
          </td>
          <td>Tang2020 - Estimation of transmission risk of COVID-19 and impact of public health interventions</td>
          <td>8</td>
          <td>16</td>
        </tr>
        <tr class="abstract-row" style="display:none;">
          <td colspan="4">
            <div class="abstract-content">
              <!-- Render HTML content from Python backend here -->
              <body xmlns="http://www.w3.org/1999/xhtml">
    <p>Since the emergence of the first cases in Wuhan, China, the novel coronavirus (2019-nCoV) infection has been quickly spreading out to other provinces and neighboring countries. Estimation of the basic reproduction number by means of mathematical modeling can be helpful for determining the potential and severity of an outbreak and providing critical information for identifying the type of disease interventions and intensity. A deterministic compartmental model was devised based on the clinical progression of the disease, epidemiological status of the individuals, and intervention measures. The estimations based on likelihood and model analysis show that the control reproduction number may be as high as 6.47 (95% CI 5.71–7.23). Sensitivity analyses show that interventions, such as intensive contact tracing followed by quarantine and isolation, can effectively reduce the control reproduction number and transmission risk, with the effect of travel restriction adopted by Wuhan on 2019-nCoV infection in Beijing being almost equivalent to increasing quarantine by a 100 thousand baseline value. It is essential to assess how the expensive, resource-intensive measures implemented by the Chinese authorities can contribute to the prevention and control of the 2019-nCoV infection, and how long they should be maintained. Under the most restrictive measures, the outbreak is expected to peak within two weeks (since 23 January 2020) with a significant low peak value. With travel restriction (no imported exposed individuals to Beijing), the number of infected individuals in seven days will decrease by 91.14% in Beijing, compared with the scenario of no travel restriction.</p>
  </body>
            </div>
          </td>
        </tr>
        
      </tbody>
    </table>
  </div>

  <div>
    <h3 id="how_to_contribute">How To Add Your Models</h3>
    <p>
      To contribute new models to the leaderboard, please follow the instructions in the <a href="docs/data/loading_model.html" target="_blank">Model Submission Guide</a> section. This guide provides the necessary steps for preparing and submitting your models, ensuring they are automatically validated and integrated into the leaderboard system via our CI/CD pipeline.
    </p>
  </div>

  <script>
    $(document).ready(function() {
      // Toggle abstract visibility on click
      $(".abstract-toggle .toggle-icon").click(function() {
        var tr = $(this).closest('tr');
        var abstractRow = tr.next('.abstract-row');
        if (abstractRow.is(":visible")) {
          abstractRow.hide();
          $(this).text('visibility_off');
        } else {
          abstractRow.show();
          $(this).text('visibility');
        }
      });
    });
  </script>
</body>
</html>
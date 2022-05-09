# WP2_pilot

Pilot study of Sgr B2 in preparation for WP2 of ACES. Below outlines the workflow
for team decomposition of the Sgr B2 data.

Workflow
--------

0. Fork the repository to your own branch
1. Clone github repo using ``git clone https://github.com/<yourusername>/WP2_pilot.git``
2. Download relevant data from globus including ``HC3N_TP_7m_12m_feather.fits``
   and ``HC3N_TP_7m_12m_feather.mask2d.fits``
3. Move data cube and mask into local repo (.gitignore will prevent them from
   being uploaded to github post-decomposition)
4. Assign issue to your name on github
5. Create a local branch using ``git checkout -b s1.XX.scousepy`` where `XX` is
   the chunk number you are wanting to decompose
6. Update ``run_scouse_chunks.py`` with relevant assigned chunk number ``XX``
7. Run ``run_scouse_chunks.py`` to completion
8. Note any problematic spectra as you go along (if there are any)
9. Once completed commit your changes (remember to tag the issue in the commit
   remarks using e.g. #1) and push to branch using ``git push origin s1.XX.scousepy``
10. Create a pull request to ``main``, again tagging the issue number in the
    comments
11. Update the issue comments with any problems encountered during fitting

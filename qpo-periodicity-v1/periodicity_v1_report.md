# Mrk 421 / Mrk 501 WCDA Periodicity Analysis v1

Generated from local pipeline outputs in `data/processed/periodicity/{mkn421,mkn501}/`. Current report date: 2026-05-21.

This version keeps the existing Mrk 421 WCDA/Fermi quick-look analysis and the Mrk 501 LHAASO-WCDA weekly light curve. It runs CWT and WWZ checks, then adds a first local-significance assessment for the current Mrk 421 and Mrk 501 WCDA weekly candidate peaks.

The updated figures use a clearer layout: the light curve is shown across the first row, while CWT and WWZ maps are separated on the second row. In the regular periodicity section after the xgm poster comparison, WWZ main displays now use linear heatmap color normalization; previous log-color versions are retained as visual references. The period axis remains log-scaled.

## Peak Summary

| Source | Series | N | MJD min | MJD max | Median dt [d] | CWT peak [d] | CWT GWS | WWZ peak [d] | WWZ power |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Mrk 421 | WCDA daily | 360 | 60763.167 | 61128.167 | 1.000 | 104.95 | 19.650 | 109.77 | 29.772 |
| Mrk 421 | WCDA weekly | 264 | 59284.333 | 61125.167 | 7.000 | 367.33 | 4.486 | 363.22 | 5.177 |
| Mrk 421 | Fermi weekly on WCDA axis | 250 | 59284.333 | 61062.167 | 7.000 | 583.10 | 2.828 | 513.37 | 3.260 |
| Mrk 501 | WCDA weekly | 264 | 59284.333 | 61125.167 | 7.000 | 389.17 | 4.407 | 402.98 | 6.385 |

## Figure Notes

- Mrk 421 WCDA daily covers 2025-03-29 04:00 UTC to 2026-03-29 04:00 UTC.
- Mrk 421 WCDA daily: CWT peak 104.95 d (GWS 19.650); WWZ peak 109.77 d (power 29.772).
- Mrk 421 WCDA weekly covers 2021-03-11 07:59 UTC to 2026-03-26 04:00 UTC.
- Mrk 421 WCDA weekly: CWT peak 367.33 d (GWS 4.486); WWZ peak 363.22 d (power 5.177).
- Mrk 421 Fermi weekly on WCDA axis covers 2021-03-11 07:59 UTC to 2026-01-22 04:00 UTC.
- Mrk 421 Fermi weekly on WCDA axis: CWT peak 583.10 d (GWS 2.828); WWZ peak 513.37 d (power 3.260).
- Mrk 501 WCDA weekly covers 2021-03-11 07:59 UTC to 2026-03-26 04:00 UTC.
- Mrk 501 WCDA weekly: CWT peak 389.17 d (GWS 4.407); WWZ peak 402.98 d (power 6.385).

The quick-look CWT/WWZ maps are not post-trial significance products. The local-significance section below gives a first local-only assessment of the current weekly candidate peaks; no look-elsewhere, source-level, or method-level trial correction is applied.

## Local-significance assessment of current candidate peaks

This section freezes the candidate peaks already visible in the Mrk 421 and Mrk 501 WCDA weekly global spectra and asks only whether those fixed peaks look locally unusual under simple red-noise null models. The WCDA series is still `wcda_flux_excess`, a photon-count/excess-rate proxy rather than a final calibrated flux product; this is a workflow pass that should be rerun when calibrated flux is available.

CWT uses `pycwt` Morlet global-wavelet-spectrum references for an AR(1) red-noise null. WWZ uses 1000 AR(1) Gaussian surrogate light curves on the same weekly sampling and reports a local-window FAP within ±10% of each candidate period. CWT and WWZ are two views of the same light curve structure, not independent discoveries. Peaks with only about 3-5 observed cycles should be treated as candidates or hints, not robust QPO detections.

| Source | Method | Period [d] | Cycles | Observed | Local FAP | 95% ref. | 99% ref. | Reading |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Mrk 421 | CWT | 129.87 | 14.17 | GWS 2.965 | — | 11.371 | 14.095 | Below AR(1) 95% local reference. |
| Mrk 421 | CWT | 367.33 | 5.01 | GWS 4.486 | — | 14.675 | 20.042 | Below AR(1) 95% local reference; only about five cycles. |
| Mrk 421 | WWZ | 135.67 | 13.57 | WWZ 4.634 | 0.4665 | 7.442 | 9.232 | Not locally unusual in the AR(1) surrogate test. |
| Mrk 421 | WWZ | 363.22 | 5.07 | WWZ 5.177 | 0.6244 | 15.565 | 21.794 | Not locally unusual in the AR(1) surrogate test. |
| Mrk 501 | CWT | 137.59 | 13.38 | GWS 1.270 | — | 3.687 | 4.593 | Below AR(1) 95% local reference. |
| Mrk 501 | CWT | 389.17 | 4.73 | GWS 4.407 | — | 4.766 | 6.545 | Close to but below the AR(1) 95% local reference; only about five cycles. |
| Mrk 501 | WWZ | 61.22 | 30.07 | WWZ 1.783 | 0.5165 | 2.500 | 2.984 | Not locally unusual in the AR(1) surrogate test. |
| Mrk 501 | WWZ | 140.87 | 13.07 | WWZ 1.761 | 0.7113 | 3.665 | 4.692 | Not locally unusual in the AR(1) surrogate test. |
| Mrk 501 | WWZ | 402.98 | 4.57 | WWZ 6.385 | 0.0310 | 5.233 | 7.726 | Passes this local 95% surrogate check but not 99%; still not a global/post-trial detection. |

Reading: in this first local-only pass, most current weekly peaks are consistent with the simple AR(1) red-noise null. The strongest exception is Mrk 501 WWZ near 403 d, with local-window FAP ≈ 0.031, but it has only about 4.6 cycles and has not been corrected for the period search, two-source comparison, or using both CWT and WWZ.


## Regular WWZ Color-Scale Comparison

Main regular figures now use linear WWZ heatmap color normalization. The Mrk 421 and Mrk 501 WCDA weekly summary figures additionally show CWT and WWZ global spectra below the 2D maps. Red dashed lines mark algorithmic candidate peaks in those global spectra; they are not significance-vetted detections.

![Mrk 421 WCDA daily linear-color WWZ](../data/processed/periodicity/mkn421/wcda_daily_periodicity.png)

Log-color reference kept for comparison:

![Mrk 421 WCDA daily log-color WWZ](../data/processed/periodicity/mkn421/wcda_daily_periodicity_logcolor.png)

![Mrk 421 WCDA weekly linear-color WWZ with global spectra](../data/processed/periodicity/mkn421/wcda_weekly_periodicity.png)

![Mrk 421 WCDA weekly CWT global spectrum local significance](../data/processed/periodicity/mkn421/wcda_weekly_cwt_global_significance.png)

![Mrk 421 WCDA weekly WWZ global spectrum local significance](../data/processed/periodicity/mkn421/wcda_weekly_wwz_global_significance.png)

Log-color reference kept for comparison:

![Mrk 421 WCDA weekly log-color WWZ with global spectra](../data/processed/periodicity/mkn421/wcda_weekly_periodicity_logcolor.png)

![Mrk 421 Fermi weekly on WCDA axis linear-color WWZ](../data/processed/periodicity/mkn421/fermi_weekly_on_wcda_axis_periodicity.png)

Log-color reference kept for comparison:

![Mrk 421 Fermi weekly on WCDA axis log-color WWZ](../data/processed/periodicity/mkn421/fermi_weekly_on_wcda_axis_periodicity_logcolor.png)

![Mrk 501 WCDA weekly linear-color WWZ with global spectra](../data/processed/periodicity/mkn501/wcda_weekly_periodicity.png)

![Mrk 501 WCDA weekly CWT global spectrum local significance](../data/processed/periodicity/mkn501/wcda_weekly_cwt_global_significance.png)

![Mrk 501 WCDA weekly WWZ global spectrum local significance](../data/processed/periodicity/mkn501/wcda_weekly_wwz_global_significance.png)

Log-color reference kept for comparison:

![Mrk 501 WCDA weekly log-color WWZ with global spectra](../data/processed/periodicity/mkn501/wcda_weekly_periodicity_logcolor.png)

## xgm poster 复现检查

Input file: `data/processed/wcda_day/LHAASO-WCDA_Mkn421_2023-06-25_2026-03-29_day.csv`.

This comparison uses `excess_counts = sum(n_on - n_bkg)` as a photon-count flux proxy. It is not a calibrated physical flux, and it is not guaranteed to be the exact same flux definition used in the xgm poster. WWZ is computed with the project helper in `src/methods/periodicity.py`; 95%/99% significance curves, red-noise simulations, and trial corrections are not reproduced in this pass.

| Window | xgm poster reported | My reproduction | Reading |
| --- | --- | --- | --- |
| 60200-60700 | 51.05 d | Global WWZ peak 111.01 d; nearest 51.05 d grid point is 49.93 d, power 12.330, rank 3 | 50 d is a strong local feature, but not the dominant peak in this run |
| 61020-61098 | 2.54, 5.2, 16.6 d | Global peak at 50.00 d upper boundary; 16.96 d ranks 3, 5.12 d ranks 10, 2.52 d is not prominent | 16.6 d has a visible counterpart; the shorter candidates are weaker here |

![xgm poster comparison, MJD 60200-60700](../data/processed/periodicity/xgm_poster_repro/mkn421/mkn421_daily_60200_60700_wwz_poster_style.png)

![xgm poster comparison, MJD 61020-61098](../data/processed/periodicity/xgm_poster_repro/mkn421/mkn421_daily_61020_61098_wwz_poster_style.png)

Interpretation: this is a comparison between the xgm poster labels and my current reproduction using the available daily `excess_counts` series. The 50 d feature appears locally in the 60200-60700 window, but my global WWZ peak is at longer periods. The short-window page shows the clearest counterpart near 16.6 d, while 2.54 d and 5.2 d are weaker in this run.

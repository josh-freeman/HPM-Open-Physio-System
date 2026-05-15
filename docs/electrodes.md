# Electrode Setup Guide

A practical, participant-facing guide for placing electrodes correctly on the HPM Open Physio System. This guide covers both the **calibration** step (no adhesive electrodes) and the **experimental session** (snap leads + hydrogel pads).

> For software, serial, or signal-quality troubleshooting, see [troubleshooting.md](troubleshooting.md).

---

## Pre-flight checklist (10-second skim)

Before the participant arrives:

- [ ] HPM box powered on and connected to the laptop via the USB data blocker
- [ ] Fresh, sealed pack of **ECG hydrogel snap electrodes** (3 per session)
- [ ] Fresh, sealed pack of **EDA pre-gelled isotonic electrodes** (2 per session)
- [ ] Alcohol prep wipes (one per skin site)
- [ ] Non-shedding gauze or paper towel
- [ ] Sharps/biohazard-style bin or sealed waste bag for used electrodes
- [ ] Spare electrodes within reach (assume one will fail)
- [ ] Participant is wearing a top that exposes the upper chest and lower ribs, or a gown

Before you press **Start Recording**:

- [ ] Calibration completed with green signal indicators
- [ ] All 3 ECG electrodes attached and snap leads clipped on
- [ ] Both EDA electrodes seated on the thenar eminence of the **non-dominant** hand
- [ ] Cables are slack, not pulling on the pads
- [ ] Participant is comfortable and informed they can stop at any time

---

## Two electrode setups, one session

The HPM workflow uses electrodes in two distinct ways. They are not interchangeable.

| | Calibration (Stage 03 "Signal Quality") | Experimental session (recording) |
|---|---|---|
| **Where** | Built-in GSR sensor pads on the HPM box | Adhesive pads on participant's skin |
| **What touches the skin** | Index + middle fingertips on conductive pads | Hydrogel (ECG) and isotonic-gel (EDA) electrodes |
| **Adhesive?** | No | Yes |
| **Gel?** | No | Pre-applied on the electrode |
| **Duration** | 30 seconds | Full session length |
| **Purpose** | Verify sensor is alive; collect a 30 s baseline | Record ECG and EDA during the task |
| **Hand used** | Either (whatever is comfortable) | Non-dominant hand for EDA |
| **Reusable?** | The box pads are reusable (wipe between participants) | No — single-use, dispose after the session |

**Key point:** The fingers-on-pads step at calibration is **not** the experimental EDA recording. The experimental EDA is recorded from gelled electrodes on the thenar eminence, not from the fingertip pads on the box.

---

## What you need

### Per session

| Item | Quantity | Notes |
|---|---|---|
| ECG hydrogel snap electrodes | 3 | Foam-backed, pre-gelled, single-use |
| EDA pre-gelled isotonic electrodes | 2 | Isotonic (not hyperosmotic) gel — matches sweat composition |
| Alcohol prep wipes (70% isopropyl) | 5 | One per skin site |
| Non-shedding gauze or paper towel | 1 | For drying skin after the wipe |
| Disposal bag or bin | 1 | Used electrodes go straight in after the session |

### Optional but useful

- Mild abrasive prep gel (e.g., Nuprep) for participants with very dry or oily skin
- Surgical tape (1 cm strips) to anchor the snap-lead cables and reduce motion artifact
- Small scissors or trimmer for participants with chest hair at ECG sites
- Hand warmers if the room is cold (cold hands give a low EDA baseline)

---

## Step 1 — Calibration (GUI Stage 03)

This is a sensor check, not an electrode placement. The participant simply rests two fingers on the box.

The GUI will display the instruction:

> *"Place your index and middle fingers on the GSR sensor pads. Keep your fingers still and relaxed. The system will collect a 30-second baseline."*

What to do:

1. Ask the participant to rest their hand on the table next to the HPM box.
2. Have them place their **index** and **middle** fingertips flat on the two metal pads on top of the box.
3. Confirm the fingers are relaxed — not pressing hard, not curled.
4. Click **Start** in the GUI. The 30-second baseline runs automatically.
5. Watch for green indicators on ECG and GSR. If either stays red, see [troubleshooting.md](troubleshooting.md).

After calibration, the participant lifts their fingers off the pads. Wipe the pads with an alcohol wipe between participants.

---

## Step 2 — Experimental ECG placement (Lead II)

Three hydrogel snap electrodes in a Lead II configuration.

### Landmarks in plain English

- **Right collarbone (positive):** the bony ridge across the top of the chest, on the participant's right side, about a thumb's width below the collarbone itself.
- **Left lower rib (negative):** on the participant's left side, just below the lowest rib, roughly in line with the nipple.
- **Ground:** right lower rib (mirror of the negative site) **or** right collarbone next to the positive site. Either works — the right lower rib gives slightly cleaner signal.

### Placement procedure

1. Wipe each of the three sites with an alcohol prep wipe. Let dry for 10 seconds.
2. Peel one ECG electrode off its backing. Hold it by the foam edge; do not touch the gel.
3. Press the electrode firmly onto the skin, gel-side down, for about 5 seconds. Smooth the foam edge so it sticks all the way around.
4. Repeat for the other two sites.
5. Snap the lead clips onto the studs:
   - **Red** lead → right collarbone (positive)
   - **Yellow** or **black** lead → left lower rib (negative)
   - **Green** or **white** lead → right lower rib (ground)
6. Anchor each cable with a 1 cm strip of surgical tape a few inches from the electrode so cable movement does not pull the pad off.

### Visual check

The leads should hang loosely without tension. The participant should be able to breathe and shift slightly without any electrode lifting at the edge.

---

## Step 3 — Experimental EDA placement (thenar eminence)

Two isotonic-gel electrodes on the **non-dominant hand**.

### Why the non-dominant hand?

The dominant hand moves more during the task — typing, mouse, button presses. Motion contaminates EDA. Use the non-dominant hand to keep the signal clean.

### What is the thenar eminence?

The fleshy mound at the base of the thumb on the palm side of the hand. Make a thumbs-up gesture — the muscle that pops out at the base of the thumb is the thenar eminence. It has a high density of eccrine sweat glands, which is exactly what EDA measures.

### Placement procedure

1. Wipe the participant's thenar eminence with an alcohol prep wipe. Dry with gauze.
2. Peel the first electrode off its backing.
3. Press it firmly onto the **upper part** of the thenar eminence, closer to the base of the thumb.
4. Place the second electrode about **2 cm** below the first, on the lower part of the same muscle. The two electrodes should be in line with the long axis of the thumb.
5. Smooth the edges of both pads so they adhere all the way around.
6. Connect the EDA snap leads. Order does not matter for EDA — the channel is bipolar.
7. Ask the participant to rest their hand palm-up on the table or armrest. The hand should be supported and still.

### Quick visual check

Both electrodes are flat against the skin, not curling at the edges. The cable runs away from the hand without pulling. The participant's fingers are relaxed.

---

## Skin preparation

Good skin prep is the single biggest predictor of clean signal. Spend 30 seconds on it.

### Standard prep (every site)

1. Wipe the site with a 70% isopropyl alcohol prep pad in a small circular motion for 5 seconds.
2. Pat dry with non-shedding gauze. Do not wait for it to air-dry under the electrode — trapped alcohol can irritate skin.
3. Apply the electrode while the skin is dry to the touch.

### Edge cases

| Situation | What to do |
|---|---|
| **Oily skin** | Wipe twice with alcohol. If still beading, lightly buff with a Nuprep-style abrasive gel. |
| **Very dry skin** | Skip the alcohol wipe entirely; it will make things worse. Wipe with a damp gauze and dry. |
| **Hairy chest at ECG sites** | Trim the hair short with scissors or a trimmer. Do not shave — micro-cuts cause artifact and irritation. |
| **Cold hands** | Have the participant rub their hands together for 30 seconds, or use a hand warmer for 1–2 minutes before placing EDA. Cold hands give a low, flat EDA baseline. |
| **Calluses on the thenar eminence** | Place the electrodes slightly to the side of the callus where the skin is thinner. |
| **Lotion or makeup at the site** | Wipe twice with alcohol. Lotion is a major contact-quality killer. |

---

## Single-use policy

**Hydrogel ECG electrodes and isotonic EDA electrodes are single-use. Do not save and reuse them.**

Why:

- Skin oils contaminate the gel after one wear, breaking down its conductivity.
- The adhesive deforms and will not stick reliably a second time.
- Re-using electrodes between participants is a hygiene violation.
- A failed seal mid-session means a wasted recording — much more expensive than a fresh electrode.

After the session, peel each electrode off, fold it sticky-side-to-itself, and drop it in the disposal bag. Wipe the snap-lead clips with an alcohol pad before storing.

The built-in GSR pads on the HPM box (used at calibration) are reusable. Wipe them with an alcohol pad between participants.

---

## Failure modes

### ECG

| Symptom | Likely cause | Fix |
|---|---|---|
| Flat line, no QRS complex | One electrode not contacting skin | Re-seat the foam; if still flat, replace the electrode |
| Wandering baseline (slow drift) | Cable tension pulling on pad | Tape the cable down a few inches from the electrode |
| Sharp 60 Hz buzz overlay | Mains interference, ground electrode bad | Replace the ground electrode; confirm participant is on battery-powered laptop |
| Huge spikes on every breath | Electrode too high on rib cage; movement | Move negative electrode lower, onto stable rib |
| BPM stuck at extreme value | R-peak detector confused by artifact | Re-prep the skin and replace electrodes; see [troubleshooting.md](troubleshooting.md) |

### EDA

| Symptom | Likely cause | Fix |
|---|---|---|
| Flat at ~0 µS, no response | Electrodes not making contact, cable disconnected | Re-seat both pads; check snap leads |
| Stuck high at ~40 µS | Audio jack not fully seated on the GSR board | See [troubleshooting.md](troubleshooting.md) — reseat the jack and click Connect again |
| Very noisy / spiky | Hand moving, or electrodes not flat against skin | Stabilize the hand on the armrest; smooth the electrode edges |
| Slow downward drift over the session | Gel drying out (rare in a 30-min session) | Replace electrodes; ensure pack was sealed before use |
| Plausible value, no responses to stimuli | Cold hands / low arousal baseline | Warm hands before recording; check the task is actually triggering arousal |

---

## Safety notes

- **Skin irritation:** If the participant reports itching, burning, or visible redness during setup, remove the electrode immediately. Mild redness after removal is normal and fades within an hour.
- **Allergies:** A small fraction of people are sensitive to the hydrogel adhesive. Ask during screening: *"Have you ever had a reaction to medical adhesive bandages or ECG stickers?"* If yes, do not run them on this hardware.
- **Broken skin:** Do not place electrodes over cuts, abrasions, rashes, eczema, or tattoos with raised ink. Move to an adjacent site.
- **Pregnancy:** Standard ECG/EDA placement is safe in pregnancy. Avoid placing the negative ECG electrode directly over the abdomen — keep it on the rib.
- **Pacemakers and implanted devices:** Do not run participants with implanted cardiac devices on this hardware without explicit clearance from the PI.
- **Stop conditions:** If the participant asks to stop, stop. Remove electrodes promptly. Do not pull hard — peel from one edge while pressing the skin down with your other hand.

---

## Quick reference

| Site | Channel | Electrode type | Most common pitfall |
|---|---|---|---|
| Index + middle fingertips on box pads | Calibration only | None (built-in pads) | Pressing too hard or moving fingers during the 30 s baseline |
| Right collarbone | ECG positive (red lead) | Hydrogel snap, single-use | Placing it on the bone itself instead of just below |
| Left lower rib | ECG negative (yellow/black lead) | Hydrogel snap, single-use | Too high — gives breathing artifact |
| Right lower rib | ECG ground (green/white lead) | Hydrogel snap, single-use | Skipped entirely; ground is required for clean ECG |
| Thenar eminence (upper), non-dominant hand | EDA channel | Pre-gelled isotonic, single-use | Placing on the fingertip out of habit |
| Thenar eminence (lower), non-dominant hand | EDA channel | Pre-gelled isotonic, single-use | Less than 2 cm spacing — pads touch and short |

---

## Related guides

- [quickstart.md](quickstart.md) — full setup from unboxing to first session
- [troubleshooting.md](troubleshooting.md) — software, serial, and signal-quality issues

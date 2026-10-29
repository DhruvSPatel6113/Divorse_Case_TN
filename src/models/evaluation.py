"""
Evaluation Metrics Module for Forecasting and Classification Models.

Complies with Section 7 (Step 5) and Section 9:
- Hand-verifiable calculations for MAE, RMSE, MAPE, Balanced Accuracy, Macro F1, Brier Score.
"""

from typing import Dict, Any, List, Tuple
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    brier_score_loss,
)


def evaluate_forecast(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Calculate forecasting metrics: MAE, RMSE, and MAPE."""
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    mae = float(mean_absolute_error(y_true, y_pred))
    rmse = float(root_mean_squared_error(y_true, y_pred))

    # Avoid zero division in MAPE
    non_zero = y_true != 0
    if np.any(non_zero):
        mape = float(np.mean(np.abs((y_true[non_zero] - y_pred[non_zero]) / y_true[non_zero])) * 100)
    else:
        mape = 0.0

    return {
        "mae": round(mae, 2),
        "rmse": round(rmse, 2),
        "mape_pct": round(mape, 2),
    }


def evaluate_classification(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: np.ndarray = None,
    class_labels: List[str] = None,
) -> Dict[str, Any]:
    """Calculate comprehensive classification metrics: Macro F1, Balanced Acc, Precision, Recall, Brier."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    acc = float(accuracy_score(y_true, y_pred))
    bal_acc = float(balanced_accuracy_score(y_true, y_pred))
    macro_f1 = float(f1_score(y_true, y_pred, average="macro", zero_division=0))
    macro_prec = float(precision_score(y_true, y_pred, average="macro", zero_division=0))
    macro_rec = float(recall_score(y_true, y_pred, average="macro", zero_division=0))

    cm = confusion_matrix(y_true, y_pred)

    per_class = {}
    classes = class_labels if class_labels else np.unique(np.concatenate([y_true, y_pred]))
    for i, cls in enumerate(classes):
        prec = float(precision_score(y_true == cls, y_pred == cls, zero_division=0))
        rec = float(recall_score(y_true == cls, y_pred == cls, zero_division=0))
        f1 = float(f1_score(y_true == cls, y_pred == cls, zero_division=0))
        per_class[str(cls)] = {
            "precision": round(prec, 3),
            "recall": round(rec, 3),
            "f1_score": round(f1, 3),
        }

    metrics = {
        "accuracy": round(acc, 4),
        "balanced_accuracy": round(bal_acc, 4),
        "macro_f1": round(macro_f1, 4),
        "macro_precision": round(macro_prec, 4),
        "macro_recall": round(macro_rec, 4),
        "confusion_matrix": cm.tolist(),
        "per_class": per_class,
    }

    if y_prob is not None and len(np.unique(y_true)) == 2:
        try:
            brier = float(brier_score_loss(y_true, y_prob[:, 1] if y_prob.ndim == 2 else y_prob))
            metrics["brier_score"] = round(brier, 4)
        except Exception:
            pass

    return metrics

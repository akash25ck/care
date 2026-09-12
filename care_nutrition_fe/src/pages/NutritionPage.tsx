import { useQuery } from "@tanstack/react-query";
import { useTranslation } from "react-i18next";

import { API } from "@/utils/api";

export default function NutritionPage() {
  const { t } = useTranslation();
  const { data, isLoading } = useQuery({
    queryKey: ["care_nutrition", "config"],
    queryFn: () => API.config(),
  });

  const metrics = [
    { label: t("nutrition__metric_growth"), value: "1,248" },
    { label: t("nutrition__metric_followup"), value: "318" },
    { label: t("nutrition__metric_supplies"), value: "94%" },
  ];

  return (
    <div className="p-6 text-slate-800">
      <header className="mb-6 space-y-2">
        <p className="text-sm font-medium uppercase tracking-wide text-emerald-700">
          {t("nutrition__eyebrow")}
        </p>
        <h1 className="text-2xl font-semibold text-slate-900">
          {t("nutrition__page_title")}
        </h1>
      </header>

      <section className="grid gap-4 md:grid-cols-3">
        {metrics.map((metric) => (
          <div key={metric.label} className="rounded-xl border border-emerald-100 bg-white p-4 shadow-sm">
            <div className="text-sm text-slate-500">{metric.label}</div>
            <div className="mt-2 text-3xl font-bold text-emerald-700">{metric.value}</div>
          </div>
        ))}
      </section>

      <section className="mt-6 rounded-xl border border-slate-200 bg-slate-50 p-5">
        <h2 className="text-lg font-semibold text-slate-900">
          {t("nutrition__programme_title")}
        </h2>
        <p className="mt-2 text-sm text-slate-600">
          {isLoading
            ? t("nutrition__loading")
            : t("nutrition__status", {
                enabled: String(data?.enabled),
              })}
        </p>
      </section>
    </div>
  );
}

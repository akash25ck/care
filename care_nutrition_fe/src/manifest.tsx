import { lazy } from "react";

import Page from "./components/Page";

const NutritionPage = lazy(() => import("./pages/NutritionPage"));

interface NavigationLink {
  url: string;
  name: string;
  icon?: React.ReactNode;
  children?: NavigationLink[];
}

interface Manifest {
  plugin: string;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  routes: Record<string, (...args: any) => React.ReactNode>;
  extends: string[];
  components: {
    FacilityHomeActions: React.LazyExoticComponent<
      React.FC<{ facility: { id: string }; className?: string }>
    >;
  };
  navItems?: NavigationLink[];
  userNavItems?: NavigationLink[];
  adminNavItems?: NavigationLink[];
}

const manifest: Manifest = {
  plugin: "care_nutrition_fe",
  routes: {
    "/nutrition": () => (
      <Page>
        <NutritionPage />
      </Page>
    ),
  },
  extends: [],
  components: {
    FacilityHomeActions: lazy(
      () => import("./components/FacilityHomeActions"),
    ),
  },
  navItems: [
    {
      url: "/nutrition",
      name: "Nutrition programmes",
    },
  ],
  userNavItems: [],
  adminNavItems: [],
};

export default manifest;

// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "publications",
          description: "publications in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "Courses I assist with at Boğaziçi University [Computer Engineering Department](https://cmpe.bogazici.edu.tr/).",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "dropdown-flow",
              title: "flow",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/flow/";
              },
            },{id: "dropdown-arts",
              title: "arts",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/arts/";
              },
            },{id: "insights-airplane-engine",
          title: 'Airplane Engine',
          description: "",
          section: "Insights",handler: () => {
              window.location.href = "/insights/airplane-engine/";
            },},{id: "insights-guru-in-creative-arts",
          title: 'Guru In Creative Arts',
          description: "",
          section: "Insights",handler: () => {
              window.location.href = "/insights/guru-in-creative-arts/";
            },},{id: "insights-small-projects-snowball",
          title: 'Small Projects Snowball',
          description: "",
          section: "Insights",handler: () => {
              window.location.href = "/insights/small-projects-snowball/";
            },},{id: "news-i-started-pursuing-my-m-sc-in-computer-engineering-at-bogazici-university",
          title: 'I started pursuing my M.Sc. in Computer Engineering at Bogazici University.',
          description: "",
          section: "News",},{id: "news-i-started-working-as-a-graduate-research-and-teaching-assistant-at-the-computer-engineering-department-at-bogazici-university",
          title: 'I started working as a Graduate Research and Teaching Assistant at the Computer...',
          description: "",
          section: "News",},{id: "news-you-can-now-play-doom-in-flow",
          title: 'You can now play doom in flow.',
          description: "",
          section: "News",},{id: "news-our-paper-noise-guided-masking-for-image-based-joint-embedding-predictive-architectures-was-accepted-at-the-34th-signal-processing-and-communications-applications-siu-conference",
          title: 'Our paper “Noise-guided Masking for Image-based Joint-Embedding Predictive Architectures” was accepted at the...',
          description: "",
          section: "News",},{id: "news-i-defended-my-master-s-thesis-at-bogazici-university-masking-for-enhanced-self-supervised-learning-in-joint-embedding-predictive-architectures",
          title: 'I defended my Master’s thesis at Bogazici University: “Masking for Enhanced Self-Supervised Learning...',
          description: "",
          section: "News",},{id: "news-you-can-view-my-sketches-in-arts",
          title: 'You can view my sketches in arts.',
          description: "",
          section: "News",},{id: "news-our-paper-noise-guided-masking-for-image-based-joint-embedding-predictive-architectures-is-now-available-on-ieee-xplore-you-can-find-it-in-publications",
          title: 'Our paper “Noise-guided Masking for Image-based Joint-Embedding Predictive Architectures” is now available on...',
          description: "",
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/assets/pdf/kutay-eroglu-CV.pdf", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6B%75%74%61%79.%65%72%6F%67%6C%75@%62%6F%67%61%7A%69%63%69.%65%64%75.%74%72", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/kutayeroglu", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/kutayeroglu", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0009-0000-3835-9383", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=aqYwtmAAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];

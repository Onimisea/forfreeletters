document.addEventListener("DOMContentLoaded", function () {
  document.body.addEventListener("htmx:load", function () {
    ("Welcome to ForfreeLetters!");

    var templateCategory;
    var templateSubcategory;
    var currentPage = 1;
    var searchQuery = "";

    // Update the year in the footer
    var currentYear = new Date().getFullYear();
    document.getElementById("footerCurrentYear").textContent = currentYear;

    const navIcon = document.getElementById("toggleNav");
    const navIcon2 = document.getElementById("toggleNav2");

    const mobile__nav = document.getElementById("mobile__nav");

    navIcon.addEventListener("click", function () {
      mobile__nav.classList.toggle("hide");
    });

    navIcon2.addEventListener("click", function () {
      mobile__nav.classList.toggle("hide");
    });

    const catebuttons = document.querySelectorAll(".cate");
    const subcatebuttons = document.querySelectorAll(".subcate");

    document.body.addEventListener("htmx:afterRequest", function (evt) {
      var target = evt.detail.target;
      var subcategoriesRawData = evt.detail.xhr.response;
      var subcategoriesData = JSON.parse(subcategoriesRawData);
      var subcategories = subcategoriesData.subcategories;

      const errorTarget = document.getElementById("newsletter-form-htmx-alert");

      if (evt.detail.successful) {
        // Successful request, clear out alert
        errorTarget.setAttribute("hidden", "true");
        errorTarget.innerText = "";
      } else if (evt.detail.failed && evt.detail.xhr) {
        // Server error with response contents, equivalent to htmx:responseError
        console.warn("Server error", evt.detail);
        const xhr = evt.detail.xhr;
        xhr;
        errorTarget.innerText = `${xhr.statusText}`;
        errorTarget.removeAttribute("hidden");
      } else {
        // Unspecified failure, usually caused by network error
        console.error("Unexpected htmx error", evt.detail);
        errorTarget.innerText =
          "Unexpected error, check your connection and try to refresh the page.";
        errorTarget.removeAttribute("hidden");
      }

      if (target.classList.contains("subcate-row")) {
        document
          .querySelector("#subcate-row")
          .classList.remove("htmx-settling");
        var subcates = "";
        for (let cat of subcategories) {
          let catData = cat
            .replace(/-/g, " ")
            .replace(/\b\w/g, (c) => c.toUpperCase());
          let catItem = `<button id="${cat}"
          class="subcate"
          hx-get="get-subcategories/cv/"
          hx-trigger="click"
          hx-target="#subcate-row"
        >
          ${catData}
        </button>`;

          subcates += catItem;
        }
        //(subcategories)
        document.querySelector("#subcate-row").innerHTML = subcates;
      }

      // Get all buttons with the class name subcate
      const subcatebuttons = document.querySelectorAll(".subcate");

      // Add event listener to each button
      subcatebuttons.forEach((button) => {
        button.addEventListener("click", () => {
          // Remove active class from all subcatebuttons
          subcatebuttons.forEach((btn) => btn.classList.remove("active"));

          // Add active class to the clicked button
          button.classList.add("active");

          templateSubcategory = button.id;

          fetchData(
            currentPage,
            searchQuery,
            templateCategory,
            templateSubcategory
          );
        });
      });
    });

    // Add event listener to each button
    catebuttons.forEach((button) => {
      button.addEventListener("click", () => {
        // Remove active class from all catebuttons
        catebuttons.forEach((btn) => btn.classList.remove("active"));

        // Add active class to the clicked button
        button.classList.add("active");

        // Get the ID of the clicked button
        templateCategory = button.id;
        templateSubcategory = "";

        // Call fetchData function with templateCategory and searchQuery
        fetchData(
          currentPage,
          searchQuery,
          templateCategory,
          templateSubcategory
        );
      });
    });

    const allTemplates = document.getElementById("all__templates");
    allTemplates.addEventListener("click", function () {
      templateCategory = "";
      templateSubcategory = "";
      currentPage = 1;
      searchQuery = "";

      fetchData(
        currentPage,
        searchQuery,
        templateCategory,
        templateSubcategory
      );

      catebuttons.forEach((button) => {
        button.classList.remove("active");
      });

      subcatebuttons.forEach((button) => {
        button.classList.remove("active");
      });
    });

    // Add event listener to search input field
    const searchInput = document.querySelector(".form-control");
    if (searchInput) {
      searchInput.addEventListener("input", function (event) {
        // Update searchQuery value
        searchQuery = event.target.value;

        // Call fetchData function with searchQuery
        fetchData(
          currentPage,
          searchQuery,
          templateCategory,
          templateSubcategory
        );
      });
    }

    // Function to fetch data from the API
    function fetchData(
      currentPage,
      searchQuery,
      templateCategory,
      templateSubcategory
    ) {
      // Construct URL with query parameters
      const baseUrl = "http://127.0.0.1:8000/api/generic-templates/";
      const queryParams = new URLSearchParams({
        page: currentPage || 1,
        category: templateCategory || "",
        subcategory: templateSubcategory || "",
        search: searchQuery || "",
      });
      const url = `${baseUrl}?${queryParams}`;

      // Fetch data from the API
      fetch(url)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          // Process the JSON response
          renderTemplates(data.results);
          renderPagination(data);
        })
        .catch((error) => {
          // Handle errors
          console.error("There was a problem with the fetch operation:", error);
        });
    }

    // Other functions such as renderTemplates and renderPagination can remain as they are
    // Function to render templates in the rows section
    function renderTemplates(templates) {
      const rowsSection = document.getElementById("templates-rows");
      rowsSection.innerHTML = ""; // Clear existing content
      templates.forEach((template) => {
        let formattedCategory;

        if (template.category === "cv") {
          formattedCategory = template.category.toUpperCase();
        } else {
          formattedCategory = template.category
            .replace(/-/g, " ")
            .replace(/\b\w/g, (c) => c.toUpperCase());
        }

        // Create HTML elements for each template and append to rowsSection
        const templateElement = `<section class="template__card">
        <img src="http://127.0.0.1:8000/${template.image_preview_url}" alt="" />
        <h3>${template.name}</h3>
        <p class="catp">${formattedCategory}</p>
        <a href="${template.file_upload_url}" download>Download</a>
      </section>`;
        rowsSection.innerHTML += templateElement;
      });
    }

    // Function to render pagination controls
    function renderPagination(data) {
      const paginationSection = document.getElementById(
        "templates__rows__pagination"
      );
      paginationSection.innerHTML = ""; // Clear existing content

      // Render previous page button
      if (data.previous) {
        const previousButton = document.createElement("button");
        previousButton.classList.add("previous__btn");
        previousButton.textContent = "Previous";

        previousButton.addEventListener("click", () => {
          currentPage = getPageNumber(data.previous);
          fetchData(currentPage);
        });
        paginationSection.appendChild(previousButton);
      }

      // Render page buttons
      const totalPages = Math.ceil(data.count / 2);
      for (let i = 1; i <= totalPages; i++) {
        const pageButton = document.createElement("button");
        pageButton.classList.add("page__btn");
        pageButton.textContent = i;

        // Get all buttons with the class name page__btn
        const buttons = document.querySelectorAll(".page__btn");

        // Add active class to the current page button
        if (i === currentPage) {
          pageButton.classList.add("active");
        }

        pageButton.addEventListener("click", () => {
          currentPage = i; // Update currentPage when a page button is clicked
          buttons.forEach((button) => {
            // Check if the button has the class name active
            if (button.classList.contains("active")) {
              // Do something with the active button
              button.classList.remove("active");
            }
          });
          fetchData(currentPage);
        });

        paginationSection.appendChild(pageButton);
      }

      // Render next page button
      if (data.next) {
        const nextButton = document.createElement("button");
        nextButton.classList.add("next__btn");
        nextButton.textContent = "Next";

        nextButton.addEventListener("click", () => {
          currentPage = getPageNumber(data.next);
          fetchData(currentPage);
        });
        paginationSection.appendChild(nextButton);
      }
    }

    // Function to extract page number from URL
    function getPageNumber(url) {
      const regex = /page=(\d+)/;
      const match = url.match(regex);
      return match ? parseInt(match[1]) : 1;
    }

    fetchData();
  });
});

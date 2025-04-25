document.addEventListener("DOMContentLoaded", function () {
    const deletedCategories = new Set();
    const deletedMenuItems = new Set();
    const deletedTables = new Set();
    const deletedSlots = new Set();

    /** -----------------------------
     *  Handle dynamically added lines
     *  (supports all buttons: new + existing)
     *  ---------------------------- */
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("add-line-btn")) {
            const categoryDiv = e.target.closest(".menu-category");
            const table = categoryDiv?.querySelector(".menu-items-table tbody");
            const emptyLine = table?.querySelector(".empty-line");

            if (table && emptyLine) {
                const newRow = emptyLine.cloneNode(true);
                newRow.style.display = "";
                newRow.classList.remove("empty-line");
                newRow.querySelectorAll("input").forEach(input => input.value = "");
                table.appendChild(newRow);
            } else {
                console.error("No .empty-line found in this category.");
            }
        }
    });

    /** -----------------------------
     *  Remove Line & Track Deletions
     *  ---------------------------- */
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-line-btn")) {
            const row = e.target.closest("tr");

            if (row.classList.contains("menu-item")) {
                const menuItemId = row.getAttribute("data-menu-item-id");
                if (menuItemId) deletedMenuItems.add(menuItemId);
            } else if (row.classList.contains("table-item")) {
                const tableId = row.getAttribute("data-table-id");
                if (tableId) deletedTables.add(tableId);
            } else if (row.classList.contains("slot-item")) {
                const slotId = row.getAttribute("data-slot-id");
                if (slotId) deletedSlots.add(slotId);
            }

            row.remove();
        }
    });

    /** -----------------------------
     *  Add New Category Block
     *  ---------------------------- */
    document.getElementById("add-category-btn").addEventListener("click", function () {
        const container = document.getElementById("menu-container");
        const html = `
          <div class="menu-category" data-category-id="new">
              <div class="d-flex justify-content-between align-items-center">
                  <h5 class="mt-3">
                      <input type="text" class="form-control editable-input category-name" placeholder="New Category">
                  </h5>
                  <button class="btn btn-danger remove-category-btn">Remove Category</button>
              </div>
              <div class="menu-items-wrapper">
                  <table class="table table-dark table-striped menu-items-table">
                      <thead>
                          <tr>
                              <th>Name</th><th>Description</th><th>Price</th><th>Actions</th>
                          </tr>
                      </thead>
                      <tbody>
                          <tr class="empty-line" style="display: none;">
                              <td><input type="text" class="form-control editable-input" id="menu-item-name" placeholder="Item Name"></td>
                              <td><input type="text" class="form-control editable-input" id="menu-item-description" placeholder="Description"></td>
                              <td><input type="number" class="form-control editable-input" id="menu-item-price" placeholder="Price"></td>
                              <td><button class="btn btn-danger remove-line-btn">Remove</button></td>
                          </tr>
                      </tbody>
                  </table>
                  <button class="btn btn-primary add-line-btn mt-2">Add Line</button>
              </div>
          </div>
        `;
        container.insertAdjacentHTML("beforeend", html);
    });

    /** -----------------------------
     *  Remove Category and track
     *  ---------------------------- */
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-category-btn")) {
            const categoryDiv = e.target.closest(".menu-category");
            const categoryId = categoryDiv.getAttribute("data-category-id");

            if (confirm("Are you sure you want to remove this category?")) {
                if (categoryId && categoryId !== "new") {
                    deletedCategories.add(categoryId);
                }
                categoryDiv.remove();
            }
        }
    });

    /** -----------------------------
     *  Save Restaurant Handler
     *  ---------------------------- */
    document.getElementById("save-btn").addEventListener("click", function () {
        const data = {
            "restaurant-name": document.getElementById("restaurant-name").value,
            phone: document.getElementById("phone").value,
            address: document.getElementById("address").value,
            description: document.getElementById("description").value,
            latitude: document.getElementById("latitude").value,
            longitude: document.getElementById("longitude").value,
            cuisine: document.getElementById("cuisine").value,
            deleted_categories: Array.from(deletedCategories),
            deleted_menu_items: Array.from(deletedMenuItems),
            new_categories: [],
            updated_categories: [],
            new_menu_items: [],
            updated_menu_items: [],
            deleted_tables: Array.from(deletedTables),
            new_tables: [],
            updated_tables: [],
            deleted_slots: Array.from(deletedSlots),
            new_slots: [],
            updated_slots: [],
        };

        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        const restaurantId = document.getElementById("save-btn").getAttribute("data-restaurant-id");

        // Gather category + menu items
        document.querySelectorAll(".menu-category").forEach((category) => {
            const categoryId = category.getAttribute("data-category-id");
            const categoryName = category.querySelector(".category-name").value;

            if (categoryId === "new") {
                data.new_categories.push({name: categoryName});
            } else {
                data.updated_categories.push({id: categoryId, name: categoryName});
            }

            category.querySelectorAll(".menu-items-table tbody tr:not(.empty-line)").forEach((row) => {
                const itemName = row.querySelector("#menu-item-name")?.value;
                const itemDescription = row.querySelector("#menu-item-description")?.value;
                const itemPrice = row.querySelector("#menu-item-price")?.value;

                if (!itemName || !itemPrice) return;

                const itemId = row.getAttribute("data-menu-item-id");

                if (categoryId === "new" || !itemId) {
                    data.new_menu_items.push({
                        category_name: categoryName,
                        name: itemName,
                        description: itemDescription,
                        price: itemPrice,
                    });
                } else {
                    data.updated_menu_items.push({
                        id: itemId,
                        category_id: categoryId,
                        name: itemName,
                        description: itemDescription,
                        price: itemPrice,
                    });
                }
            });
        });

        // Gather tables
        document.querySelectorAll("#table-info tbody tr:not(.empty-line)").forEach((row) => {
            const tableId = row.getAttribute("data-table-id");
            const number = row.querySelector("td:nth-child(1) input")?.value;
            const capacity = row.querySelector("td:nth-child(2) input")?.value;

            if (!number || !capacity) return;

            const payload = {number, capacity};

            tableId
                ? data.updated_tables.push({id: tableId, ...payload})
                : data.new_tables.push(payload);
        });

        // Gather slots
        document.querySelectorAll("#available-slots tbody tr:not(.empty-line)").forEach((row) => {
            const slotId = row.getAttribute("data-slot-id");
            const time = row.querySelector("#slot-item-time")?.value;
            const date = row.querySelector("#slot-item-date")?.value;
            const table_id = row.querySelector("#slot-table-number")?.value;

            if (!time || !date || !table_id) return;

            const payload = {time, date, table_id};

            slotId
                ? data.updated_slots.push({id: slotId, ...payload})
                : data.new_slots.push(payload);
        });

        console.log("Data to save:", data);

        fetch(`/restaurant/${restaurantId}/save/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify(data),
        })
            .then(res => {
                if (res.ok) {
                    alert("Changes saved!");
                    deletedCategories.clear();
                    deletedMenuItems.clear();
                    deletedTables.clear();
                    deletedSlots.clear();
                } else {
                    alert("Failed to save.");
                }
            })
            .catch(err => {
                console.error("Save error:", err);
            });
    });
});
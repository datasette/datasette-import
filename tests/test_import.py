from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_create_table_permissions():
    datasette = Datasette()
    datasette.add_memory_database("test")
    anon_response = await datasette.client.get("/test")
    assert anon_response.status_code == 200
    fragment = ">Create table with imported data"
    assert fragment not in anon_response.text
    root_response = await datasette.client.get(
        "/test", cookies={"ds_actor": datasette.client.actor_cookie({"id": "root"})}
    )
    assert root_response.status_code == 200
    assert fragment in root_response.text
    # And check access to the /-/import page
    anon_import_response = await datasette.client.get("/test/-/import")
    assert anon_import_response.status_code == 403
    root_import_response = await datasette.client.get(
        "/test/-/import",
        cookies={"ds_actor": datasette.client.actor_cookie({"id": "root"})},
    )
    assert root_import_response.status_code == 200

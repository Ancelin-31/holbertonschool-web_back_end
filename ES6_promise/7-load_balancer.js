export default async function loadBalancer(chinaDownload, USDownload) {
    promise1 = chinaDownload(resolve, reject);
    promise2 = USDownload(resolve, reject);

    const Promises = [promise1, promise2];
    Promise.race(Promises).then((value) => {
        return value;
    });
}